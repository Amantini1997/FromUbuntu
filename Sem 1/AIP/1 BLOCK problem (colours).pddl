(define 
    (problem coloured-blocks) 
    (:domain BLOCKS)
    (:objects 
                A B C           - block
                HAND            - hand
                RED BLUE GREEN - colour
    )

    (:init
        (ontable B)
        (clear B)
        (block-colour B BLUE)
        (ontable C)
        (block-colour C RED)
        (on A C)
        (clear A)
        (block-colour A GREEN)
        (handempty)
        (washed HAND)
    )

    (:goal (and
        (on A B)
        (on B C)
        (ontable C)
    ))

    ;un-comment the following line if metric is needed
    ;(:metric minimize (???))
)
