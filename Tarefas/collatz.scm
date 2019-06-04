#lang scheme

(define (collatz_cond n)
  (cond 
    ((= n 1) (cons 1 null))
    ((even? n) (cons n (collatz (/ n 2))))
    (#t (cons n (collatz (+ 1 (* 3 n)))))
    ))



(define (collatz n)
  (if (= n 1)
      (cons 1 null)  
      (if (even? n) 
          (cons n (collatz (/ n 2)))
          (cons n (collatz (+ 1 (* 3 n)))))))



(collatz 13)