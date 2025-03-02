import json
import csv


CSV_HEADER = [
        'Card ID', 'Card Name', 'Card URL', 'Card Description', 'Labels', 'Members', 'Due Date', 'Attachment Count',
        'Attachment Links', 'Checklist Item Total Count', 'Checklist Item Completed Count', 'Vote Count', 'Comment Count',
        'Last Activity Date', 'List ID', 'List Name', 'Board ID', 'Board Name', 'Archived', 'Start Date', 'Due Complete'
    ]


# Load the Trello JSON file
with open('trello_board.json') as f:
    trello_data = json.load(f)

# Create a CSV file
with open('trello_board.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Define the CSV headers for the structure you provided
    writer.writerow(CSV_HEADER)

    # Iterate through the Trello data and write it to the CSV
    for card in trello_data['cards']:
        # Extract relevant card data
        card_id = card['id']
        card_name = card['name']
        card_url = f"https://trello.com/c/{card_id}"
        card_description = card.get('desc', '')
        
        # Extract labels (joined by commas)
        labels = ', '.join([label['name'] for label in card.get('labels', [])])
        
        # Extract members (users assigned to the card)
        members = ', '.join([member['fullName'] for member in card.get('assigned', [])]) if card.get('assigned') else ''
        
        # Extract due date
        due_date = card.get('due', '')
        
        # Attachment count (assuming the 'attachments' field exists; modify as needed)
        attachment_count = len(card.get('attachments', []))
        attachment_links = ', '.join([attachment['url'] for attachment in card.get('attachments', [])])
        
        # Checklist item counts
        checklist_item_count = sum(len(checklist['checkItems']) for checklist in card.get('checklists', []))
        checklist_item_completed_count = sum(sum(1 for item in checklist['checkItems'] if item['state'] == 'complete') for checklist in card.get('checklists', []))
        
        # Vote count (if present)
        vote_count = card.get('badges', {}).get('votes', 0)
        
        # Comment count
        comment_count = card.get('badges', {}).get('comments', 0)
        
        # Last activity date
        last_activity_date = card.get('dateLastActivity', '')
        
        # Extract list information
        list_id = card.get('idList', '')
        list_name = next((lst['name'] for lst in trello_data['lists'] if lst['id'] == list_id), '')  # Get the list name based on the list ID
        
        # Board details (assuming you're exporting from a single board)
        board_id = trello_data.get('id', '')
        board_name = trello_data.get('name', '')
        
        # Archived status (if present)
        archived = card.get('closed', False)
        
        # Start date
        start_date = card.get('dateStart', '')
        
        # Due complete (True or False if the task is completed)
        due_complete = card.get('dueComplete', False)

        # Write the card data to a row in the CSV
        writer.writerow([
            card_id, card_name, card_url, card_description, labels, members, due_date, attachment_count,
            attachment_links, checklist_item_count, checklist_item_completed_count, vote_count, comment_count,
            last_activity_date, list_id, list_name, board_id, board_name, archived, start_date, due_complete
        ])
