package Lab3;

public class Lab3NoSync {
    // Константа, определяющая количество итераций для каждого потока
    public static final int ITERATIONS = 100000;
    
    // Общий счетчик, который будет инкрементироваться и декрементироваться потоками
    private static int counter = 0;

    public static void main(String[] args) {
        // Количество потоков, инкрементирующих счетчик
        int n = 5;
        // Количество потоков, декрементирующих счетчик
        int m = 5;

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

        // Вывод значения счетчика и времени выполнения
        System.out.println("Значение счётчика: " + counter);
        System.out.println("Время выполнения: " + executionTime + " ms");
    }

    // Класс задачи, инкрементирующей счетчик
    static class IncrementTask implements Runnable {
        @Override
        public void run() {
            for (int i = 0; i < ITERATIONS; i++) {
                int localCounter = counter;
                localCounter++;
                counter = localCounter;
            }
        }
    }

    // Класс задачи, декрементирующей счетчик
    static class DecrementTask implements Runnable {
        @Override
        public void run() {
            for (int i = 0; i < ITERATIONS; i++) {
                int localCounter = counter;
                localCounter--;
                counter = localCounter;
            }
        }
    }
}
