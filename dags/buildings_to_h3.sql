DROP TABLE IF EXISTS tbilisi_buildings_bbox_h3;

CREATE TABLE IF NOT EXISTS tbilisi_buildings_bbox_h3 AS
SELECT h3_cell_to_boundary_geometry(h3_polygon_to_cells(ST_Buffer(ST_Envelope(geometry)::geography,400)::geometry,8))   
FROM tbilisi_buildings;