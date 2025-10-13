package com.itheima;/*
package com.itheima;

// 定义Animal类
class Animal {
    private String name;         			 //声明name属性
    private int age;             			 //声明age属性
    public final String COLOR = "黑色";       //定义COLOR属性
    public String getName() {                //定义name属性的getter方法
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {                    //定义age属性的getter方法
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }
}
// 定义Dog类继承Animal类
class Dog extends Animal {
    //此处不写任何代码
}
// 定义测试类
public class Example01 {
    public static void main(String[] args) {
        Dog dog = new Dog();        //创建一个Dog类的对象
        dog.setName("牧羊犬");       //此时调用的是父类Animal中的setter方法
        dog.setAge(3);              //此时调用的是父类Animal中的setter方法
        System.out.println("名称："+dog.getName()+",年龄："+dog.getAge()
                +",颜色："+dog.COLOR);
    }
}
*/
