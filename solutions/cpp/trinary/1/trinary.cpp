#include "trinary.h"
#include <string>
namespace trinary {
int exponent(int num, int exponent){
    int result{1};
    for (int i{0}; i < exponent; i++){
        result *= num;
    }
    return result;
}
int to_decimal(const std::string& num){
    int len{static_cast<int>(num.length())};
    int decimal_num{0};
    for (int i{0}; i < len; i++){
        int n {static_cast<int>(num[i] - '0')};
        if (n >= 0 && n <= 2) decimal_num += exponent(3, (len -1 - i)) * n; // to handle invalid inputs
    }
    return decimal_num;
}

}  // namespace trinary
