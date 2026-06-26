#include "darts.h"

namespace darts {
int score (double x, double y){
    const double distance_squared = (x*x) + (y*y);
    if (distance_squared <= 1.0)   return 10;
    if (distance_squared <= 25.0)  return 5;
    if (distance_squared <= 100.0) return 1;
    else                           return 0;
}
}  // namespace darts