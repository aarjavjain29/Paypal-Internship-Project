import pandas as pd
import sys
import os

def find_header_row(df):
    for i in range(min(10, len(df))):
        row = df.iloc[i]
        non_null_count = row.notna().sum()
        if non_null_count > len(df.columns) * 0.5:
            return i
    return 0

def excel_to_markdown(excel_file, sheet_number, output_file=None):
    if not os.path.exists(excel_file):
        print(f"Error: File '{excel_file}' not found")
        return False
    
    try:
        xl = pd.ExcelFile(excel_file)
        if sheet_number < 1 or sheet_number > len(xl.sheet_names):
            print(f"Error: Sheet number {sheet_number} is out of range (1-{len(xl.sheet_names)})")
            print(f"Available sheets: {xl.sheet_names}")
            return False
        
        sheet_name = xl.sheet_names[sheet_number - 1]
        print(f"Processing sheet: {sheet_name}")
        
        df_raw = pd.read_excel(excel_file, sheet_name=sheet_name, header=None)
        
        header_row = find_header_row(df_raw)
        print(f"Found headers at row {header_row + 1}")
        
        
        df = pd.read_excel(excel_file, sheet_name=sheet_name, header=header_row)
        
        
        df.columns = [str(col).replace('\n', ' ').strip() if pd.notna(col) else f'Column_{i}' 
                     for i, col in enumerate(df.columns)]
        
       
        df = df.dropna(how='all')
        
        
        df = df.fillna('')
        
        
        markdown_content = f"# {sheet_name} Data\n\n"
        markdown_content += f"**Source:** {os.path.basename(excel_file)}\n"
        markdown_content += f"**Sheet:** {sheet_name}\n"
        markdown_content += f"**Total Rows:** {len(df)}\n"
        markdown_content += f"**Total Columns:** {len(df.columns)}\n\n"
        
        
        if len(df) > 0:
            
            headers = "| " + " | ".join(df.columns) + " |\n"
            separator = "| " + " | ".join(["---"] * len(df.columns)) + " |\n"
            
            markdown_content += headers + separator
            
           
            for _, row in df.iterrows():
                row_data = []
                for cell in row:
                    
                    cell_str = str(cell) if pd.notna(cell) and cell != '' else ''
                    cell_str = cell_str.replace('|', '\\|').replace('\n', '<br>')
                    row_data.append(cell_str)
                markdown_content += "| " + " | ".join(row_data) + " |\n"
        else:
            markdown_content += "*No data found in this sheet*\n"
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            print(f"Markdown table saved to: {output_file}")
        else:
            print("\n" + "="*50)
            print(markdown_content)
            print("="*50)
        
        return True
        
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return False

def main():
    excel_file = "MTL- query results.xlsx"  
    sheet_number = 2             
    
    base_name = os.path.splitext(excel_file)[0] 
    output_file = f"{base_name}_sheet{sheet_number}.md"
    
    success = excel_to_markdown(excel_file, sheet_number, output_file)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()