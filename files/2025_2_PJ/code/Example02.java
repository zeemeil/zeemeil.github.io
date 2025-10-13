package com.itheima;/*
package com.itheima;

// 定义Animal类
class Animal {
    private String name;         		// 声明name属性
   private int age;             		// 声明age属性
    public String getName() {
        return name;
   }
   public void setName(String name) {
       this.name = name;
    }
   public int getAge() {
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }
}
// 定义Dog类继承Animal类
class Dog extends Animal {
    private String color;        // 声明color属性
    public String getColor() {
        return color;
       }
   public void setColor(String color) {
        this.color = color;
    }
}
// 定义测试类
public class Example02 {
    public static void main(String[] args) {
        Dog dog = new Dog(); // 创建并实例化dog对象
        dog.setName("牧羊犬");// 此时访问的是父类Animal中的setter方法
        dog.setAge(3);       // 此时访问的是父类Animal中的setter方法
        dog.setColor("黑色");// 此时访问的是Dog类中的setter方法
        System.out.println("名称："+dog.getName()+",年龄："+dog.getAge()+
                ",颜色："+dog.getColor());
    }
}
*/
