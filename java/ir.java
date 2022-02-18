public class ir {

    public static void main(String[] args) {
        // NOTE: The following input values are used for testing your solution.

        int[] array1 = { 1, 2, 3, 4, 5, 6, 7 };
        int[] array2 = { 4, 5, 6, 7, 0, 2, 3 };

        System.out.print("is rotation:");
        System.out.print(isRotation(array1, array2));
    }

    private static boolean isRotation(int[] array1, int[] array2) {
        if (array1.length != array2.length)
            return false;

        int p2 = 0;

        while (p2 < array2.length) {
            if (array1[0] == array2[p2]) {
                break;
            }
            p2++;
        }

        if (p2 == array2.length)
            return false;

        for (int p1 = 0; p1 < array1.length; p1++) {
            if (array1[p1] != array2[p2]) {
                return false;
            }

            p2 = (p2 < array2.length-1) ? p2 + 1 : 0;
        }

        return true;
    }
}
