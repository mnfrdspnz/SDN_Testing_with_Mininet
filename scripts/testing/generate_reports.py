import os
import glob
import pandas as pd

def collect_logs(log_directory):
    """Collect log data from specified directory."""
    log_files = glob.glob(os.path.join(log_directory, '*.log'))
    logs = {}
    for log_file in log_files:
        with open(log_file, 'r') as file:
            logs[os.path.basename(log_file)] = file.readlines()
    return logs

def generate_report(logs, report_file):
    """Generate a report from collected logs."""
    report_data = []
    for log_file, log_lines in logs.items():
        for line in log_lines:
            report_data.append((log_file, line.strip()))
    df = pd.DataFrame(report_data, columns=['LogFile', 'LogEntry'])
    df.to_csv(report_file, index=False)
    print(f"Report generated: {report_file}")

def main():
    log_directory = './scripts/testing/logs'
    report_file = 'test_report.csv'
    logs = collect_logs(log_directory)
    generate_report(logs, report_file)

if __name__ == '__main__':
    main()

