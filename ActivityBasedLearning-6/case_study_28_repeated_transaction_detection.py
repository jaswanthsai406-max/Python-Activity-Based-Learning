# Priority #6 - Case Study 28: Repeated Transaction Detection
# Objective: Detect potential duplicate or fraud transactions within a given time threshold.

from datetime import datetime

def find_repeated_transactions(transactions, time_threshold_seconds=60):
    duplicates = []
    # Sort transactions by timestamp
    sorted_txs = sorted(transactions, key=lambda x: datetime.strptime(x['timestamp'], "%Y-%m-%d %H:%M:%S"))
    
    for i in range(len(sorted_txs)):
        for j in range(i + 1, len(sorted_txs)):
            t1, t2 = sorted_txs[i], sorted_txs[j]
            t1_time = datetime.strptime(t1['timestamp'], "%Y-%m-%d %H:%M:%S")
            t2_time = datetime.strptime(t2['timestamp'], "%Y-%m-%d %H:%M:%S")
            
            time_diff = (t2_time - t1_time).total_seconds()
            if time_diff > time_threshold_seconds:
                break
                
            if t1['account'] == t2['account'] and t1['amount'] == t2['amount']:
                duplicates.append((t1, t2, time_diff))
                
    return duplicates

def main():
    txs = [
        {"id": 101, "account": "ACC_1", "amount": 5000, "timestamp": "2026-11-04 10:00:00"},
        {"id": 102, "account": "ACC_1", "amount": 5000, "timestamp": "2026-11-04 10:00:45"},
        {"id": 103, "account": "ACC_2", "amount": 1200, "timestamp": "2026-11-04 10:05:00"},
        {"id": 104, "account": "ACC_1", "amount": 5000, "timestamp": "2026-11-04 10:15:00"}
    ]
    
    flagged = find_repeated_transactions(txs, time_threshold_seconds=60)
    print("Flagged Duplicate Transactions:")
    for t1, t2, diff in flagged:
        print(f" - Flagged Tx {t1['id']} and Tx {t2['id']} for Account {t1['account']} (${t1['amount']}) within {diff}s")

if __name__ == "__main__":
    main()
