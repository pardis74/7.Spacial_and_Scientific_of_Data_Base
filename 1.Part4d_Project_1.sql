SELECT 
  Driver.DriverLicenseNumber, --WE need to select the drivers, So we select them by the DriverLicenseNumber
  COUNT(*) AS num_trips, 
  CASE 
    WHEN EXTRACT(HOUR FROM Call_T.callTime) BETWEEN 0 AND 11 THEN 'Morning'
    WHEN EXTRACT(HOUR FROM Call_T.callTime) BETWEEN 12 AND 17 THEN 'Afternoon'
    WHEN EXTRACT(HOUR FROM Call_T.callTime) BETWEEN 18 AND 23 THEN 'Evening'
  END AS part_of_day
FROM 
  Driver 
  JOIN DriveBy ON Driver.DriverLicenseNumber = DriveBy.DriverLicenseNumber 
  JOIN Call_T ON DriveBy.PlateNumber = Call_T.PlateNumber --This joint is for finding the time of daythe drivers are working
WHERE 
  Call_T.callTime >= NOW() - INTERVAL '3' DAY --Check for the last 3 days
GROUP BY 
  Driver.DriverLicenseNumber, 
  part_of_day 
ORDER BY 
  num_trips DESC;
