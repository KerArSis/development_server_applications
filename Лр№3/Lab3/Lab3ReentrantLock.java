package Lab3;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.concurrent.locks.ReentrantLock;

public class Lab3ReentrantLock {
    // Константа, определяющая количество итераций для каждого потока
    public static final int ITERATIONS = 100000;
    // Общий счетчик, который будет инкрементироваться и декрементироваться потоками
    private static int counter = 0;
    // Переменная блокировки ReentrantLock для синхронизации доступа к счетчику
    private static final ReentrantLock lock = new ReentrantLock();

    public static void main(String[] args) {
        // Массив количества потоков для тестирования
        int[] threadCounts = { 1, 2, 4, 8 };

        // Создание файла для вывода результатов
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("Lab8.txt"))) {
            writer.write("Streams (n, m) | Counter | Time (мс)\n");

            // Цикл по количеству потоков инкрементирующих и декрементирующих счетчик
            for (int n : threadCounts) {
                for (int m : threadCounts) {
                    // Замер времени начала выполнения
                    long startTime = System.currentTimeMillis();

                    // Массивы потоков, инкрементирующих и декрементирующих счетчик
                    Thread[] incrementThreads = new Thread[n];
                    Thread[] decrementThreads = new Thread[m];

                    // Создание и запуск потоков, инкрементирующих счетчик
                    for (int i = 0; i < n; i++) {
                        incrementThreads[i] = new Thread(new IncrementTask());
                        incrementThreads[i].start();
                    }

                    // Создание и запуск потоков, декрементирующих счетчик
                    for (int i = 0; i < m; i++) {
                        decrementThreads[i] = new Thread(new DecrementTask());
                        decrementThreads[i].start();
                    }

                    // Ожидание завершения всех потоков
                    try {
                        for (int i = 0; i < n; i++) {
                            incrementThreads[i].join();
                        }
                        for (int i = 0; i < m; i++) {
                            decrementThreads[i].join();
                        }
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }

                    // Замер времени окончания выполнения
                    long endTime = System.currentTimeMillis();
                    long executionTime = endTime - startTime;

                    // Запись результатов в файл
                    writer.write(String.format("(%d, %d) | %d | %d ms\n", n, m, counter, executionTime));
                    counter = 0; // сброс счетчика для следующего запуска
                }
            }

            // Вывод информации о системе
            writer.write("\nCPU: " + System.getProperty("os.arch") + "\n");
            writer.write("RAM: " + Runtime.getRuntime().totalMemory() / (1024 * 1024) + " MB\n");
            writer.write("OC: " + System.getProperty("os.name") + " " + System.getProperty("os.version") + "\n");

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Класс задачи, инкрементирующей счетчик с использованием ReentrantLock
    static class IncrementTask implements Runnable {
        @Override
        public void run() {
            for (int i = 0; i < ITERATIONS; i++) {
                lock.lock();
                counter++;
                lock.unlock();
            }

        }
    }

    // Класс задачи, декрементирующей счетчик с использованием ReentrantLock
    static class DecrementTask implements Runnable {
        @Override
        public void run() {
            for (int i = 0; i < ITERATIONS; i++) {
                lock.lock();
                counter--;
                lock.unlock();
            }
        }
    }
}
