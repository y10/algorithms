import java.io.InvalidObjectException;
import java.security.InvalidAlgorithmParameterException;

public class ms {
    public static void main(String[] args) {
        // NOTE: The following input values will be used for testing your solution.
        int[][] bombs1 = { { 0, 2 }, { 2, 0 } };
        mineSweeperTest(bombs1, 3, 3, new int[][] {
                new int[] { 0, 1, -1 },
                new int[] { 1, 2, 1 },
                new int[] { -1, 1, 0 }
        });

        int[][] bombs2 = { { 0, 0 }, { 0, 1 }, { 1, 2 } };
        mineSweeperTest(bombs2, 3, 4, new int[][] {
                new int[] { -1, -1, 2, 1 },
                new int[] { 2, 3, -1, 1 },
                new int[] { 0, 1, 1, 1 }
        });

        int[][] bombs3 = { { 1, 1 }, { 1, 2 }, { 2, 2 }, { 4, 3 } };
        // mineSweeperTest(bombs3, 5, 5);
        // [[1, 2, 2, 1, 0],
        // [1, -1, -1, 2, 0],
        // [1, 3, -1, 2, 0],
        // [0, 1, 2, 2, 1],
        // [0, 0, 1, -1, 1]]
    }

    public static void setBomb(int[][] field, int r, int c) {
        if (r >= 0 && c >= 0 && r < field.length && c < field[r].length && field[r][c] != -1) {
            field[r][c] += 1;
        }
    }

    // Implement your solution below.
    public static int[][] mineSweeper(int[][] bombs, int numRows, int numCols) {
        int[][] field = new int[numRows][numCols];

        for (int[] point : bombs) {
            int r = point[0];
            int c = point[1];
            setBomb(field, r - 1, c - 1);
            setBomb(field, r - 1, c);
            setBomb(field, r - 1, c + 1);
            setBomb(field, r, c - 1);
            field[r][c] = -1;
            setBomb(field, r, c + 1);
            setBomb(field, r + 1, c - 1);
            setBomb(field, r + 1, c);
            setBomb(field, r + 1, c + 1);
        }

        return field;
    }

    public static void mineSweeperTest(int[][] bombs, int numRows, int numCols, int[][] result) {

        int[][] field = mineSweeper(bombs, numRows, numCols);

        boolean failed = false;
        for (int r = 0; r < numRows; r++) {
            for (int c = 0; c < numCols; c++) {
                System.out.print(field[r][c]);
                System.out.print(' ');
                if (field[r][c] != result[r][c]) {
                    failed = true;
                }
            }
            System.out.println();
        }

        if (failed)
            System.out.println("FAILED");
        else
            System.out.println("SUCCESSED");
    }

}
