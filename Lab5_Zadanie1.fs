let rec fib n =
    if n <=1 then n
    else fib(n-1) + fib(n-2)

let wynik = fib 4
printf "rek fib z 4: %d" wynik

let fibTail n =
    let rec aux n a b =
        match n with
        | 0 -> a
        | _ -> aux (n - 1) b (a + b)
    aux n 0 1

let wynik1 = fibTail 5
printf "rek fibTail z 5: %d" wynik1
