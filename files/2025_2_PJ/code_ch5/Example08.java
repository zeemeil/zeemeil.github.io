package com.itheima;

 class DivideByMinusException extends Exception{
    public DivideByMinusException (){
        super();          	// 调用Exception无参的构造方法
    }
    public DivideByMinusException (String message){
        super(message); 	// 调用Exception有参的构造方法
    }
}

public class Example08 {
    public static void main(String[] args) {
        int result = divide(4, -2);
        System.out.println(result);
    }
    //下面的方法实现了两个整数相除
    public static int divide(int x, int y) {
        if(y<0){
           // throw new DivideByMinusException("除数是负数");
        }
        int result = x / y;   	// 定义一个变量result记录两个数相除的结果
        return result;         	// 将结果返回
    }
}