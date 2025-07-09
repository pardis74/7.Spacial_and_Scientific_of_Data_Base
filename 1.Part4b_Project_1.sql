--We use the district column of the region table and after that we will use 
SELECT district, 
       CASE --Case Statement is for categorize the pick up and drop off times in to 4 category
         WHEN EXTRACT(HOUR FROM StartTime) >= 5 AND EXTRACT(HOUR FROM StartTime) < 12 THEN 'Morning' 
         WHEN EXTRACT(HOUR FROM StartTime) >= 12 AND EXTRACT(HOUR FROM StartTime) < 17 THEN 'Afternoon' 
         WHEN EXTRACT(HOUR FROM StartTime) >= 17 AND EXTRACT(HOUR FROM StartTime) < 22 THEN 'Evening' 
         ELSE 'Night' 
       END AS part_of_day, 
       COUNT(DISTINCT PickUp) AS pickups, --Counting the pickups
       COUNT(DISTINCT DropOff) AS dropoffs --Counting the dropoffs
FROM   TaxiLocation 
       JOIN Region ON ST_Contains(Region.RCoordinator, TaxiLocation.TCoordinator) --In here we need to check if taxi is in the region (ST_Contains for checking that one object is inside the another object)
GROUP  BY district, 
          CASE 
            WHEN EXTRACT(HOUR FROM StartTime) >= 5 AND EXTRACT(HOUR FROM StartTime) < 12 THEN 'Morning' 
            WHEN EXTRACT(HOUR FROM StartTime) >= 12 AND EXTRACT(HOUR FROM StartTime) < 17 THEN 'Afternoon' 
            WHEN EXTRACT(HOUR FROM StartTime) >= 17 AND EXTRACT(HOUR FROM StartTime) < 22 THEN 'Evening' 
            ELSE 'Night' 
          END;
