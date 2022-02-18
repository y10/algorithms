import java.util.HashMap;
import java.util.PriorityQueue;

import classes.Item;

public class mf {

    public static void main(String[] args) {
        // NOTE: The following input values are used for testing your solution.

        // mostFrequent(array1) should return 1.
        int[] array1 = { 1, 3, 1, 3, 2, 1 };
        int result1 = mostFreqent(array1);
        System.out.println(result1 == 1 ? "SUCCESS" : "FAILURE");
        // mostFrequent(array2) should return 3.
        int[] array2 = { 3, 3, 1, 3, 2, 1 };
        int result2 = mostFreqent(array2);
        System.out.println(result2 == 3 ? "SUCCESS" : "FAILURE");
        // mostFrequent(array3) should return null.
        int[] array3 = {};
        Integer result3 = mostFreqent(array3);
        System.out.println(result3 == null ? "SUCCESS" : "FAILURE");
        // mostFrequent(array4) should return 0.
        int[] array4 = { 0 };
        Integer result4 = mostFreqent(array4);
        System.out.println(result4 == 0 ? "SUCCESS" : "FAILURE");
        // mostFrequent(array5) should return -1.
        int[] array5 = { 0, -1, 10, 10, -1, 10, -1, -1, -1, 1 };
        int result5 = mostFreqent(array5);
        System.out.println(result5 == -1 ? "SUCCESS" : "FAILURE");
    }

    public static Integer mostFreqent(int[] givenArray) {
        var nums = new HashMap<Integer, Integer>();

        Integer maxCount = 0;
        Integer freqNumber = null;
        for (int i : givenArray) {
            int count = nums.getOrDefault(i, 0) + 1;
            if (maxCount < count) {
                maxCount = count;
                freqNumber = i;
            }

            nums.put(i, count);
        }

        return freqNumber;
    }

    // Implement your solution below.
    public static Integer mostFreqent2(int[] givenArray) {
        var nums = new HashMap<Integer, Integer>();

        for (int i : givenArray) {
            nums.put(i, nums.getOrDefault(i, 0) + 1);
        }

        var pq = new PriorityQueue<Item>();
        nums.forEach((value, count) -> pq.add(new Item(count, value)));

        if (!pq.isEmpty())
            return pq.peek().value;

        return null;
    }
}
