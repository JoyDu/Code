using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 内置委托Func和Action
{
    class Program
    {
        static void Main(string[] args)
        {
            Action<string> ac = new Action<string>(new Program().SayHello);
            ac("Joydu");
            Func<string> fc = new Func<string>(new Program().GetName);
            string name = fc();
            Console.WriteLine(string.Format("My Name is {0}", name));
            Console.ReadKey();
        }
        public void SayHello(string name)
        {
            Console.WriteLine(string.Format("Hello {0}",name));
        }
        public string GetName()
        {
            return "Joydu";
        }
    }
    
}
