import java.util.ArrayDeque;

public class msc {
    public static void main(String[] args) {
        // NOTE: The following input values will be used for testing your solution.
        int[][] field1 = { 
                { 0, 0, 0, 0, 0 },
                { 0, 1, 1, 1, 0 },
                { 0, 1, -1, 1, 0 } };

        test_click(field1, 3, 5, 2, 2, new int[][] {
                { 0, 0, 0, 0, 0 },
                { 0, 1, 1, 1, 0 },
                { 0, 1, -1, 1, 0 }
        });

        test_click(field1, 3, 5, 1, 4, new int[][] {
                { -2, -2, -2, -2, -2 },
                { -2, 1, 1, 1, -2 },
                { -2, 1, -1, 1, -2 }
        });

        int[][] field2 = { { -1, 1, 0, 0 },
                { 1, 1, 0, 0 },
                { 0, 0, 1, 1 },
                { 0, 0, 1, -1 } };

        test_click(field2, 4, 4, 0, 1, new int[][] {
                { -1, 1, 0, 0 },
                { 1, 1, 0, 0 },
                { 0, 0, 1, 1 },
                { 0, 0, 1, -1 }
        });

        test_click(field2, 4, 4, 1, 3, new int[][] {
                { -1, 1, -2, -2 },
                { 1, 1, -2, -2 },
                { -2, -2, 1, 1 },
                { -2, -2, 1, -1 }
        });

    }

    // Implement your solution below.
    public static int[][] click(int[][] field, int numRows, int numCols, int givenRow, int givenCol) {

        ArrayDeque<int[]> q = new ArrayDeque<int[]>();
        if (field[givenRow][givenCol] == 0) {
            q.add(new int[] { givenRow, givenCol });
        }

        while (!q.isEmpty()) {
            int[] p = q.pop();
            int r = p[0];
            int c = p[1];

            if (field[r][c] == 0) {
                field[r][c] = -2;
            }

            for (int i = (r - 1); i <= (r + 1); i++) {
                for (int j = (c - 1); j <= (c + 1); j++) {
                    if ((i >= 0) && (j >= 0) && (i < numRows) && (j < numCols)) {
                        if (field[i][j] == 0) {
                            q.add(new int[] { i, j });
                        }
                    }
                }
            }
        }

        return field;
    }

    public static void test_click(int[][] givenField, int numRows, int numCols, int givenI, int givenJ,
            int[][] expectedField) {

        int[][] resultField = click(givenField, numRows, numCols, givenI, givenJ);

        boolean failed = false;
        for (int r = 0; r < numRows; r++) {
            for (int c = 0; c < numCols; c++) {
                System.out.print(resultField[r][c]);
                System.out.print(' ');
                if (resultField[r][c] != expectedField[r][c]) {
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
