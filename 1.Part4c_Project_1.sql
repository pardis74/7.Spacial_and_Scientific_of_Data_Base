SELECT 
  c.MobileNumber, --at first we need find the customers by the mobile phone, so we select the customer by mobile number
  COUNT(*) as num_trips
FROM 
  Customer c
  JOIN Call_T ct ON c.MobileNumber = ct.MobileNumber --We will join the customer and it's Call_Time
WHERE 
  ct.callTime BETWEEN NOW() - INTERVAL '2 WEEK' AND NOW() --We need to check the number of calls for the last 2 weeks ago
GROUP BY 
  c.MobileNumber; --In the end we group by it to make it more organized