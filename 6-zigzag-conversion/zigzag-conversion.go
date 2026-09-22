func convert(s string, numRows int) string {
    if numRows == 1 || numRows >= len(s) {
        return s
    }

    rows := make([]strings.Builder, numRows)
    currRow := 0
    step := -1

    for i := 0; i < len(s); i++ {
        rows[currRow].WriteByte(s[i])

        if currRow == 0 || currRow == numRows-1 {
            step = -step
        }

        currRow += step
    }

    var result strings.Builder
    result.Grow(len(s))
    for i := 0; i < numRows; i++ {
        result.WriteString(rows[i].String())
    }

    return result.String()

}