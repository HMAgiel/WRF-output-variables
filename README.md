# WRF output variables

This is the code and txt file to remove some variables in WRF. This txt file is used before `./real.exe` and included in `namelist.input` under the `time_control` section.

All the variables shown in the txt file are the ones that are excluded, and the ones not in there will be included in the output file.

The `0` in the txt file indicates that this variable is excluded in stream 0 (history run).

Example `namelist.input` under the `&time_control` configuration:

```
&time_control
 run_days                            = 1,
 run_hours                           = 0,
 run_minutes                         = 0,
 run_seconds                         = 0,
 start_year                          = 2024, 2024, 2024,
 start_month                         = 12,   12,   12,
 start_day                           = 01,   01,   01,
 start_hour                          = 00,   00,   00,
 end_year                            = 2024, 2024, 2024,
 end_month                           = 12,   12,   12,
 end_day                             = 02,   02,   02,
 end_hour                            = 00,   00,   00,
 interval_seconds                    = 10800
 input_from_file                     = .true.,.true.,.true.,
 history_interval                    = 180,  60,   60,
 frames_per_outfile                  = 1000, 1000, 1000,
 restart                             = .false.,
 restart_interval                    = 7200,
 io_form_history                     = 2
 io_form_restart                     = 2
 io_form_input                       = 2
 io_form_boundary                    = 2
 iofields_filename                   ="WRF_Variables_exclude.txt"
 ignore_iofields_warning             =.true.
```
the last two line in the time_control above is the one that must be added to exclude the variables
