(define (problem roverprefs) 
(:domain Rover)

(:objects

	general - Lander

	colour high_res low_res - Mode

	rover0 - Rover

	rover0store - Store

	waypoint0 waypoint1 waypoint2 waypoint3 - Waypoint

	camera0 - Camera

	objective0 objective1 - Objective

	)

(:init

        ;static predicates

	(visible waypoint1 waypoint0)

	(visible waypoint0 waypoint1)

	(visible waypoint2 waypoint0)

	(visible waypoint0 waypoint2)

	(visible waypoint2 waypoint1)

	(visible waypoint1 waypoint2)

	(visible waypoint3 waypoint0)

	(visible waypoint0 waypoint3)

	(visible waypoint3 waypoint1)

	(visible waypoint1 waypoint3)

	(visible waypoint3 waypoint2)

	(visible waypoint2 waypoint3)

	

        (visible_from objective0 waypoint0)

	(visible_from objective0 waypoint1)

	(visible_from objective0 waypoint2)

	(visible_from objective0 waypoint3)

	(visible_from objective1 waypoint0)

	(visible_from objective1 waypoint1)

	(visible_from objective1 waypoint2)

	(visible_from objective1 waypoint3)

	

	(can_traverse rover0 waypoint1 waypoint0)

	(can_traverse rover0 waypoint0 waypoint1)

	(can_traverse rover0 waypoint2 waypoint0)

	(can_traverse rover0 waypoint0 waypoint2)

	(can_traverse rover0 waypoint2 waypoint1)

	(can_traverse rover0 waypoint1 waypoint2)

	(can_traverse rover0 waypoint3 waypoint0)

	(can_traverse rover0 waypoint0 waypoint3)

	(can_traverse rover0 waypoint3 waypoint1)

	(can_traverse rover0 waypoint1 waypoint3)

	(can_traverse rover0 waypoint3 waypoint2)

	(can_traverse rover0 waypoint2 waypoint3)

	

	(store_of rover0store rover0)

	(at_lander general waypoint0)

	(equipped_for_soil_analysis rover0)

	(equipped_for_rock_analysis rover0)

	(equipped_for_imaging rover0)

	(on_board camera0 rover0)

        (calibration_target camera0 objective1)

	(supports camera0 colour)

	(supports camera0 high_res)

	

        ;dynamic predicates

	(channel_free general)

	(at rover0 waypoint3)

	(available rover0)

	(empty rover0store)

	

        (at_soil_sample waypoint0)

	(at_rock_sample waypoint1)

	(at_soil_sample waypoint2)

	(at_rock_sample waypoint2)

	(at_soil_sample waypoint3)

	(at_rock_sample waypoint3)

)

(:goal (and

        (communicated_soil_data waypoint2)

        (communicated_rock_data waypoint3)

        (communicated_image_data objective1 high_res)

        ; a goal preference named g0 (cost 4) that we have communicated the image data of a colour image of objective 1 
        (preference g0 (at end (communicated_image_data objective1 colour)))

        ; a goal preference named g1 (cost 5) that the rover is at the waypoint the lander is located at
        (and (preference g1 (at end (at rover0 waypoint0)(at_lander general waypoint0)))
	)

)

(:constraints

         (and

            ; a preference named t0 (cost 2) that the rover does not return to waypoint2 if it has already been there 
            (preference t0 (at-most-once (at rover0 waypoint2)))


            ; a preference named t1 (cost 3) that at some point during the plan we have communicated data about a soil sample taken at waypoint0
            (preference t1 (sometime (communicated_soil_data waypoint0)))

            ; a preference named t2 (cost 1) that if the rover has a soil sample from waypoint0 it must have taken a rock sample at waypoint1 first 
; xxxxxx
            (preference t2 (sometime-before (have_soil_analysis rover0 waypoint0)(have_rock_analysis rover0 waypoint0)))

            ; a preference named t3 (cost 4) that if the rover has taken a soil sample at waypoint0 it must subsequently empty its store
; xxxxxx
            (preference t3 (sometime-after (have_soil_analysis rover0 waypoint0)(empty rover0store)))

            ; a preference named t4 (cost 4) that the rover does not visit waypoint1
            (preference t4 (always (not (at rover0 waypoint1))))

         )

)


; DONE
(:metric minimize

         (+ (* (is-violated g0) 4 ) ; cost for g0

            (* (is-violated g1) 5 ) ; cost for g1

            (* (is-violated t0) 2 ) ; cost for t0

            (* (is-violated t1) 3 ) ; cost for t1

            (* (is-violated t2) 1 ) ; cost for t2

            (* (is-violated t3) 4 ) ; cost for t3

            (* (is-violated t4) 4 ) ; cost for t4
         )            
)

) 

