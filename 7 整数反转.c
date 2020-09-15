int reverse(int x) {
    long long result = 0;//题目规定了int是32位的，要考虑反转数字后溢出。因此用64位long long型来防止数字溢出，再与强制转换成int的结果比较，可以知道有没有发生溢出。
    while (x != 0) {
        result = result * 10 + x % 10;//这里不需要考虑负数的余数，正常运算即可。
        x /= 10;
    }
    if ((int)result != result) { result = 0; }
    return (int)result;
}
//https://leetcode-cn.com/problems/reverse-integer/