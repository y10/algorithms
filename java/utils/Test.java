package utils;

import java.util.function.Supplier;

public class Test {
    public static void testit(Supplier<Character> fn, Character c){
        var result = fn.get();
        System.out.print(result);
        System.out.print(" ");
        System.out.println(result == c ? "SUCCESSED" : "FAILED");
    }
    
    public static void isTrue(Supplier<Boolean> fn){
        System.out.println(fn.get() ? "SUCCESSED" : "FAILED");
    }  

    public static void isFalse(Supplier<Boolean> fn){
        System.out.println(!fn.get() ? "SUCCESSED" : "FAILED");
    }  
}