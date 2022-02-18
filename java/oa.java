import utils.Test;

public class oa {
    public static void main(String[] args) {
        // NOTE: The following input values will be used for testing your solution.
        Test.isTrue(() -> isOneAway("abcdef", "abqdef")); // should return true
        Test.isTrue(() -> isOneAway("abcdef", "abccef")); // should return true
        Test.isTrue(() -> isOneAway("abcde", "abcd")); // should return true
        Test.isTrue(() -> isOneAway("abde", "abcde")); // should return true
        Test.isTrue(() -> isOneAway("a", "a")); // should return true
        Test.isTrue(() -> isOneAway("abcdef", "abcde")); // should return true
        Test.isFalse(() -> isOneAway("aaa", "abc")); // should return false
        Test.isFalse(() -> isOneAway("abcde", "abc")); // should return false
        Test.isFalse(() -> isOneAway("abc", "abcde")); // should return false
        Test.isFalse(() -> isOneAway("abc", "bcc")); // should return false
    }

    // Implement your solution below.
    public static Boolean isOneAway(String s1, String s2) {
        if (Math.abs(s1.length() - s2.length()) > 1)
            return false;

        if (s1.length() != s2.length()) {
            String l = s1;
            String r = s2;

            if (s1.length() > s2.length()) {
                l = s2;
                r = s1;
            }

            for (int i = 0; i < r.length(); i++) {

                if (i < l.length() && l.charAt(i) != r.charAt(i)) {
                    l = l.substring(0, i) + r.charAt(i) + l.substring(i);
                    return r.equals(l);
                } else if (i == l.length()) {
                    r = r.substring(0, i);
                    return r.equals(l);
                }
            }
        } else if (s1.length() == s2.length()) {

            for (int i = 0; i < s1.length(); i++) {
                if (s1.charAt(i) != s2.charAt(i)) {
                    s1 = s1.substring(0, i) + s2.charAt(i) + s1.substring(i+1);
                    break;
                }
            }
        }

        return s1.equals(s2);
    }
}
