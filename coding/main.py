from tkinter import messagebox 
import pandas as pd
import plotly as py
import plotly.graph_objs as go

from input import *
# from utils import *

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
"Description": This function plots Bias Chart with `er_plot_trace_count` traces v/s Date.
"x": wafer_id (x-axis) for Bias Chart
"y1": DICD (y-axis) for Bias Chart
"y2": FICD (y-axis) for Bias Chart
"y3": Bias (y-axis) for Bias Chart
"dicd_remarks": Date for DICD
"ficd_remarks": Date for FICD
"plot_title": Plot title
"plot_html_filename": HTML filename for plot
"""
def draw_plotly_bias_plot(x, y1, y2, y3, dicd_remarks, ficd_remarks, plot_title, plot_html_filename):
    trace1 = go.Scatter(
            x = x,
            y = y1,
            name = dicd_name,
            mode = dicd_mode, # 'lines+markers',
            line = dict(
                    color = dicd_line_color,
                    width = 2),
            marker = dict(
                    color = dicd_marker_color,
                    size = 8,
                    line = dict(
                        color = marker_border_color,
                        width = 0.5),
                    ),
            text = dicd_remarks
    )

    trace2 = go.Scatter(
            x = x,
            y = y2,
            name = ficd_name,
            mode = ficd_mode, # 'lines+markers',
            line = dict(
                    color = ficd_line_color,
                    width = 2),
            marker = dict(
                    color = ficd_marker_color,
                    size = 8,
                    line = dict(
                        color = ficd_marker_border_color,
                        width = 0.5),
                    ),
            text = ficd_remarks
    )

    trace3 = go.Scatter(
            x = x,
            y = y3,
            name = bias_name,
            mode = bias_mode, # 'lines+markers',
            line = dict(
                    color = bias_line_color,
                    width = 2),
            marker = dict(
                    color = bias_marker_color,
                    size = 8,
                    line = dict(
                        color = bias_marker_border_color,
                        width = 0.5),
                    ),
            # text = remarks
    )


    data = [trace1, trace2, trace3]
    layout = dict(
            title = plot_title,
            xaxis = dict(title= plot_xlabel),
            yaxis = dict(title= plot_ylabel)
        )
    fig = dict(data= data, layout= layout)
    py.offline.plot(fig, filename= plot_html_filename)


# ==========================================================================================
def main():
    tables = pd.read_html('../data/Data.xls')       # returns a list of tables
    df = tables[0]      # first element of the list
    # print(df)
    # df.to_excel('output.xlsx', index=False)

    df_iso = df[df[dicd_param_col_name] == 'DICD_AA_Iso_Line_Mean']
    df_iso.sort_values(by= [dicd_waferid_col_name], inplace= True)  # sorting dataframe in ascending order(by default) for waferid   
    # print(df_iso)
    df_dense = df[df[dicd_param_col_name] == 'DICD_AA_Dns_Line_Mean']
    df_dense.sort_values(by= [dicd_waferid_col_name], inplace= True)     # sorting dataframe in ascending order(by default) for waferid

    # print(df_dense)
    """
    Ensure the 2 pair of columns ['Lot ID', 'lot ID'] & ['Wafer_1', 'Wafer_2']entries match, i.e. one column of DICD
    & the other of FICD.
    """
    dicd_lotid_list = df[dicd_lotid_col_name].tolist()      # DICD lot id list
    ficd_lotid_list = df[ficd_lotid_col_name].tolist()      # FICD lot id list
    dicd_waferid_list = df[dicd_waferid_col_name].tolist()  # DICD wafer id list
    ficd_waferid_list = df[ficd_waferid_col_name].tolist()  # FICD wafer id list

    if (dicd_lotid_list == ficd_lotid_list):
        if (dicd_waferid_list == ficd_waferid_list):
            # -------------------------ISO--------------------------------
            df_iso_wafer_id = df_iso[dicd_waferid_col_name]
            df_iso_dicd = df_iso[dicd_val_col_name]
            df_iso_ficd = df_iso[ficd_val_col_name]
            df_iso_bias = df_iso[bias_val_col_name]
            df_iso_dicd_date = df_iso[dicd_date]
            df_iso_ficd_date = df_iso[ficd_date]

            draw_plotly_bias_plot(
                x = df_iso_wafer_id,
                y1 = df_iso_dicd,
                y2 = df_iso_ficd,
                y3 = df_iso_bias,
                dicd_remarks = df_iso_dicd_date,
                ficd_remarks = df_iso_ficd_date,
                plot_title = plot_title_iso,
                plot_html_filename = plot_html_filename_iso)

            #------------------------------------DENSE------------------------------
            df_dense_wafer_id = df_dense[dicd_waferid_col_name]
            df_dense_dicd = df_dense[dicd_val_col_name]
            df_dense_ficd = df_dense[ficd_val_col_name]
            df_dense_bias = df_dense[bias_val_col_name]
            df_dense_dicd_date = df_dense[dicd_date]
            df_dense_ficd_date = df_dense[ficd_date]

            draw_plotly_bias_plot(
                x = df_dense_wafer_id,
                y1 = df_dense_dicd,
                y2 = df_dense_ficd,
                y3 = df_dense_bias,
                dicd_remarks = df_dense_dicd_date,
                ficd_remarks = df_dense_ficd_date,
                plot_title = plot_title_dense,
                plot_html_filename = plot_html_filename_dense)

        else:
            master = Tk()
            master.withdraw()
            messagebox.showinfo('ERROR', 'SORRY! wafer_id column entries of \'DICD\' and \'FICD\' not matching. \nPlease rectify and try again... ')

    else:
        master = Tk()
        master.withdraw()
        messagebox.showinfo('ERROR', 'SORRY! lot_id column entries of \'DICD\' and \'FICD\' not matching. \nPlease rectify and try again... ')


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# MAIN Function call
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    try:
        main()
    except ModuleNotFoundError:
        master = Tk()
        master.withdraw()
        messagebox.showinfo('Exception ERROR', e)
    except Exception as e:
        master = Tk()
        master.withdraw()
        messagebox.showinfo('Error', 'something else happened' + str(e))

