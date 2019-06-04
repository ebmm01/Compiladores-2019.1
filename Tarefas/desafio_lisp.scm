#lang scheme

(define (fact x)
  (if (<= x 1)
    1
    (* x (fact (- x 1) ))
  )
)


(define (fact_c x acc)
  (if (<= x 1)
    acc
    (fact_c (- x 1) (* x acc))
  )
)

(define (loop n max)
  (if (> n max)
    1
    (begin
      (begin (display (fizzbuzz n)) (newline))
      (loop (+ n 1) max))
  ))

(define (fizzbuzz n)
  (cond 
    ((= (remainder n 6) 0) "FizzBuzz")
    ((= (remainder n 2) 0) "Fizz")
    ((= (remainder n 3) 0) "Buzz")
    (#t n)
  )
)

(loop 1 100)