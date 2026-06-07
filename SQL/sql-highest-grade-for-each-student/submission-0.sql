SELECT 
    e.student_id, 
    MIN(e.exam_id) AS exam_id, 
    e.score
FROM exam_results e
INNER JOIN (
    -- Step 1: Find the absolute highest score for each student
    SELECT student_id, MAX(score) AS max_score
    FROM exam_results
    GROUP BY student_id
) top_scores 
    ON e.student_id = top_scores.student_id 
    AND e.score = top_scores.max_score
-- Step 2: Group again to grab the minimum exam_id in case of ties
GROUP BY e.student_id, e.score
ORDER BY e.student_id ASC;