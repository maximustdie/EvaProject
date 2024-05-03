function updateTable() {
  fetch('/cpu/get-cpu-loads/')
    .then(response => response.json())
    .then(data => {
      const table = document.getElementById('data-table');
      const tableHead = table.querySelector('thead');
      const tableBody = table.querySelector('tbody');

      tableHead.innerHTML = '';
      tableBody.innerHTML = '';

      const headerRow = document.createElement('tr');
      data.fields.forEach(fieldName => {
        const headerCell = document.createElement('th');
        headerCell.textContent = fieldName;
        headerRow.appendChild(headerCell);
      });
      tableHead.appendChild(headerRow);

      data.cpu_loads.forEach(rowData => {
        const row = document.createElement('tr');
        Object.values(rowData).forEach(cellData => {
          const cell = document.createElement('td');
          cell.textContent = cellData;
          row.appendChild(cell);
        });
        tableBody.appendChild(row);
      });
    })
    .catch(error => console.error('Error fetching data:', error));
}

document.addEventListener('DOMContentLoaded', () => {
  updateTable();
  setInterval(updateTable, 10000);
});


