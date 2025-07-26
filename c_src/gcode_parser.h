#ifndef GCODE_PARSER_H
#define GCODE_PARSER_H

// Return codes
#define GCODE_SUCCESS              0
#define GCODE_ERROR_FILE_NOT_FOUND -1
#define GCODE_ERROR_NO_COORDINATES -2

/**
 * Extract bounding box coordinates from a G-code file
 * 
 * @param file_path Path to the G-code file (.gcode, .nc, etc.)
 * @param min_x Pointer to store minimum X coordinate
 * @param max_x Pointer to store maximum X coordinate  
 * @param min_y Pointer to store minimum Y coordinate
 * @param max_y Pointer to store maximum Y coordinate
 * @return GCODE_SUCCESS on success, error code on failure
 */
int get_bounding_box(const char* file_path,
                     double* min_x,
                     double* max_x,
                     double* min_y,
                     double* max_y);

/**
 * Update bounding box from a single line of G-code
 * 
 * @param line Line of G-code to parse
 * @param min_x Pointer to minimum X coordinate
 * @param max_x Pointer to maximum X coordinate
 * @param min_y Pointer to minimum Y coordinate  
 * @param max_y Pointer to maximum Y coordinate
 */
void update_bbox_from_line(const char* line,
                           double* min_x,
                           double* max_x,
                           double* min_y,
                           double* max_y);

#endif // GCODE_PARSER_H