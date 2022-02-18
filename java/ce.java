import java.util.ArrayList;

public class ce {

    public static void main(String[] args) {
        // NOTE: The following input values are used for testing your solution.

        int[] array1 = { 1, 3, 4, 6, 7, 9 };
        int[] array2 = { 1, 2, 4, 5, 9, 10 };

        System.out.print("[");
        for (int i : commonElements(array1, array2)) {
            System.out.print(" " + i);
        }
        System.out.print("]");
    }

    private static Integer[] commonElements(int[] array1, int[] array2) {
        int maxLength = Math.max(array1.length, array2.length);
        ArrayList<Integer> list = new ArrayList<Integer>(maxLength);

        int l = 0;
        int r = 0;

        while (l < array1.length && r < array2.length) {
            if (array1[l] == array2[r]) {
                list.add(array1[l]);
                l++;
                r++;
            } else if (array1[l] < array2[r]) {
                l++;
            } else {
                r++;
            }
        }

        Integer[] array = new Integer[list.size()];
        return list.toArray(array);
    }
}
