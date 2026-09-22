func reverse(x int) int {
var res int32 = 0
    val := int32(x)

    for val != 0 {
        pop := val % 10
        val /= 10

        if res > math.MaxInt32/10 || (res == math.MaxInt32/10 && pop > 7) {
            return 0
        }

        if res < math.MinInt32/10 || (res == math.MinInt32/10 && pop < -8) {
            return 0
        }

        res = res*10 + pop
    }

    return int(res)
}