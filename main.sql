CREATE TABLE maqsadlar (
    id INT PRIMARY KEY,
    nomi VARCHAR(255),
    maqsad TEXT
);

CREATE TABLE malumot (
    id INT PRIMARY KEY,
    nomi VARCHAR(255),
    maqsad_id INT,
    malumot TEXT,
    FOREIGN KEY (maqsad_id) REFERENCES maqsadlar(id)
);

CREATE PROCEDURE chunklab_qaytar(
    IN chunk_size INT
)
BEGIN
    DECLARE current_id INT;
    SET current_id = 0;
    WHILE current_id < (SELECT COUNT(*) FROM malumot) DO
        SELECT * FROM malumot
        WHERE id BETWEEN current_id AND current_id + chunk_size;
        SET current_id = current_id + chunk_size + 1;
    END WHILE;
END;

DELIMITER //
CREATE PROCEDURE malumotni_qaytar()
BEGIN
    CALL chunklab_qaytar(10);
END//
DELIMITER ;

INSERT INTO maqsadlar (id, nomi, maqsad) VALUES
(1, 'Maqsad 1', 'Malumot chunklab qaytarish'),
(2, 'Maqsad 2', 'Malumotni qaytarish'),
(3, 'Maqsad 3', 'Chunklab qaytarish');

INSERT INTO malumot (id, nomi, maqsad_id, malumot) VALUES
(1, 'Malumot 1', 1, 'Malumot matni 1'),
(2, 'Malumot 2', 1, 'Malumot matni 2'),
(3, 'Malumot 3', 2, 'Malumot matni 3'),
(4, 'Malumot 4', 3, 'Malumot matni 4'),
(5, 'Malumot 5', 1, 'Malumot matni 5'),
(6, 'Malumot 6', 2, 'Malumot matni 6'),
(7, 'Malumot 7', 3, 'Malumot matni 7'),
(8, 'Malumot 8', 1, 'Malumot matni 8'),
(9, 'Malumot 9', 2, 'Malumot matni 9'),
(10, 'Malumot 10', 3, 'Malumot matni 10'),
(11, 'Malumot 11', 1, 'Malumot matni 11'),
(12, 'Malumot 12', 2, 'Malumot matni 12'),
(13, 'Malumot 13', 3, 'Malumot matni 13'),
(14, 'Malumot 14', 1, 'Malumot matni 14'),
(15, 'Malumot 15', 2, 'Malumot matni 15');

CALL malumotni_qaytar();