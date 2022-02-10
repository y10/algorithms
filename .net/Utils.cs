using System.IO;
using System.Diagnostics;

public class Utils
{
    public static void Mesure(Action fn)
    {
        var sw = Stopwatch.StartNew();
        fn();
        sw.Stop();
        Console.WriteLine($"Completed in {sw.ElapsedMilliseconds}ms.");
    }

    public static void Testit<T>(Func<T> fn, Func<T, bool> assert)
    {
        var sw = Stopwatch.StartNew();
        T r = fn();
        sw.Stop();
        Console.WriteLine($"{(assert(r)? "Successfully" : "Failed to be")} completed in {sw.ElapsedMilliseconds}ms.");
    }
}