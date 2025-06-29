SELECT c.MobileNumber, th.PlateNumber, ST_Distance(c.C_Coordinator, th.TCoordinator) AS distance, r.district --MobileNumber for each Customer -> c.MobileNumber
--PlateNumber for each Taxi -> t.PlateNumber
--Computing distance between two objects (Polygon and Point)
FROM Customer c
LEFT JOIN Call_T ct ON c.MobileNumber = ct.MobileNumber --We need to check all the customers using their mobile phone to call the taxi , so we need to join table Call_T and customer
JOIN TaxiHas th ON th.TCoordinator && ST_Buffer(c.C_Coordinator, 10000) --We need to find available taxis within 10000 meters of the customer so we use the ST_Buffer (ST_Buffer" for finding buffer around Customer's location, We can find all the availbel taxi's by a specific radius. I consider radius to 10000)
LEFT JOIN TaxiLocation tl ON th.TCoordinator = tl.TCoordinator AND tl.EndTime IS NULL --We need to exclude taxis currently on a ride and we need to consider thse taxis EndTime is NULL
LEFT JOIN Region r ON r.RCoordinator && c.C_Coordinator
WHERE ct.MobileNumber IS NULL -- exclude customers currently on a ride
ORDER BY distance
LIMIT 5; --List Five closest Taxis
