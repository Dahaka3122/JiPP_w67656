type Tree<'T> =
    | Empty
    | Node of 'T * Tree<'T> * Tree<'T>

let rec findRecursive value tree =
    match tree with
    | Empty -> false
    | Node(v, left, right) ->
        if v = value then true
        else findRecursive value left || findRecursive value right

let findIterative value tree =
    let rec loop stack =
        match stack with
        | [] -> false
        | Empty :: rest -> loop rest
        | Node(v, left, right) :: rest ->
            if v = value then true
            else loop (left :: right :: rest)
    loop [tree]

