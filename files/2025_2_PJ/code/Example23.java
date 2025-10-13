package com.itheima;

interface Animal{					//定义接口Animal
    void shout();					//定义抽象方法shout()
}
public class Example23{
    public static void main(String[] args){
        String name = "小花";
        animalShout(new Animal(){	//调用animalShout()方法，参数为匿名内部类
            @Override
            public void shout() {
                System.out.println(name+"喵喵……");
            }
        });
    }
    public static void animalShout(Animal an){	//该方法参数为Animal接口类型
        an.shout();
    }
}
