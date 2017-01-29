SELECT candidato
      ,creado
      ,DATE_TRUNC('week', creado) AS creado_semana
      ,DATE_TRUNC('week', creado) AS sem
      ,fav
      ,rt
      ,texto
      ,CASE WHEN texto ILIKE '%http%' = True THEN 1 ELSE 0 END AS url
      ,CASE WHEN texto ILIKE '%#%' = True THEN 1 ELSE 0 END AS hashtag
      ,CASE WHEN texto ILIKE '%?%' = True THEN 1 ELSE 0 END AS pregunta
      ,CASE WHEN texto ILIKE '%!%' = True THEN 1 ELSE 0 END AS exclamacion
      ,CASE WHEN texto ILIKE '%@%' = True THEN 1 ELSE 0 END AS mention
      ,CASE WHEN texto ILIKE '%empleo%' = True THEN 1 ELSE 0 END AS empleo
FROM ignacio_chavarria.tweets_candidatos_ecu 
ORDER BY creado DESC
