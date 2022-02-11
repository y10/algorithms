using System.IO;
using System.Diagnostics;

public static class Utils
{
    public static void Mesure(Action fn)
    {
        var sw = Stopwatch.StartNew();
        fn();
        sw.Stop();
        Console.WriteLine($"Completed in {sw.ElapsedMilliseconds}ms.");
    }

    public static void Assert<T>(Func<T> fn, Func<T, bool> assert)
    {
        var sw = Stopwatch.StartNew();
        T r = fn();
        sw.Stop();
        Console.WriteLine($"{(assert(r) ? "Successfully" : "Failed to be")} completed in {sw.ElapsedMilliseconds}ms.");
    }

    public static Test<T> Testit<T>(Func<T> fn)
    {
        return new Test<T>(fn);
    }
}