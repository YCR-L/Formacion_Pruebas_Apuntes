using System;

    public class AddOrSubtract{

    public static int Calculate(int firstNumber, int secondNumber)

    {

        //int firstNumber;
        //int secondNumber;
        int result;

        if (firstNumber <= secondNumber)
        
        {
            result = firstNumber + secondNumber;
            Console.WriteLine(result);

        }else{
            result = firstNumber - secondNumber;
            Console.WriteLine(result);
        }
        return result;

    }
}