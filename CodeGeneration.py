from goto import with_goto

@with_goto
def range(start, stop):
    i = start
    result = []

    label .begin
    if i == stop:
        goto .end

    result.append(i)
    i += 1
    goto .begin

    label .end
    return result

if __name__ == "__main__":
    # Teste a função range()
    start = 1
    stop = 6
    result = range(start, stop)
    print("Resultado da função range():", result)