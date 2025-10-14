package com.itheima;

public class Example07 {
    // 定义printAge()输出年龄
    public static void printAge(int age) throws Exception {
        if(age <= 0){
            // 对业务逻辑进行判断，当输入年龄为负数时抛出异常
            throw new Exception("输入的年龄有误，必须是正整数！");
        }else {
            System.out.println("此人年龄为："+age);
        }
    }
    public static void main(String[] args)  {
        // 下面的代码定义了一个try…catch语句用于捕获异常
        int age = -1;
        try {
            printAge(age);
        } catch (Exception e) {  // 对捕获到的异常进行处理
            System.out.println("捕获的异常信息为：" + e.getMessage());
        }
    }
}