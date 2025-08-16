CREATE EXTENSION IF NOT EXISTS h3;
CREATE EXTENSION IF NOT EXISTS postgis_raster CASCADE;
CREATE EXTENSION IF NOT EXISTS h3_postgis CASCADE;

-- dedupe h3 cells (гексы накладываются друг на друга)
-- собрать в один пайплайн осм интерспепт популейшн 
