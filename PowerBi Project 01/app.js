// Dashboard data
const dashboardData = {
  kpis: {
    totalRevenue: "$385,522.02",
    totalGrossIncome: "$127,724.25", 
    totalTransactions: "1,200",
    avgTransaction: "$321.27",
    grossMargin: "33.1%"
  },
  branchData: [
    {"branch": "Branch B", "city": "Los Angeles", "revenue": 142281.48, "transactions": 429},
    {"branch": "Branch C", "city": "Chicago", "revenue": 123299.25, "transactions": 387},
    {"branch": "Branch A", "city": "New York", "revenue": 119941.29, "transactions": 384}
  ],
  productData: [
    {"category": "Fashion Accessories", "revenue": 67564.27, "transactions": 200, "rating": 6.92},
    {"category": "Food and Beverages", "revenue": 65929.88, "transactions": 200, "rating": 6.95},
    {"category": "Sports and Travel", "revenue": 64691.60, "transactions": 213, "rating": 7.04},
    {"category": "Health and Beauty", "revenue": 63679.94, "transactions": 213, "rating": 6.94},
    {"category": "Home and Lifestyle", "revenue": 61927.08, "transactions": 180, "rating": 7.03},
    {"category": "Electronic Accessories", "revenue": 61729.25, "transactions": 194, "rating": 6.94}
  ],
  monthlyData: [
    {"month": "Jan", "revenue": 37576.81, "transactions": 109},
    {"month": "Feb", "revenue": 25842.76, "transactions": 85},
    {"month": "Mar", "revenue": 31640.24, "transactions": 106}, 
    {"month": "Apr", "revenue": 26444.36, "transactions": 86},
    {"month": "May", "revenue": 31545.66, "transactions": 105},
    {"month": "Jun", "revenue": 33837.89, "transactions": 108},
    {"month": "Jul", "revenue": 27134.22, "transactions": 93},
    {"month": "Aug", "revenue": 36094.59, "transactions": 106},
    {"month": "Sep", "revenue": 33450.31, "transactions": 97},
    {"month": "Oct", "revenue": 36938.04, "transactions": 103},
    {"month": "Nov", "revenue": 37404.94, "transactions": 113},
    {"month": "Dec", "revenue": 27612.20, "transactions": 89}
  ],
  customerData: {
    member: {"revenue": 194139.78, "transactions": 606, "percentage": 50.4},
    normal: {"revenue": 191382.24, "transactions": 594, "percentage": 49.6}
  },
  paymentData: [
    {"method": "Ewallet", "revenue": 135808.45, "percentage": 35.2},
    {"method": "Cash", "revenue": 129171.69, "percentage": 33.5},
    {"method": "Credit Card", "revenue": 120541.88, "percentage": 31.3}
  ]
};

// Chart colors from design system
const chartColors = ['#1FB8CD', '#FFC185', '#B4413C', '#ECEBD5', '#5D878F', '#DB4545', '#D2BA4C', '#964325', '#944454', '#13343B'];

// Chart instances
let branchChart, productChart, monthlyChart, paymentChart;

// Initialize dashboard when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
  // Add small delay to ensure DOM is fully ready
  setTimeout(() => {
    initializeCharts();
    attachEventListeners();
    updateLastRefreshed();
  }, 100);
});

// Initialize all charts
function initializeCharts() {
  initializeBranchChart();
  initializeProductChart();
  initializeMonthlyChart();
  initializePaymentChart();
}

// Branch Performance Chart
function initializeBranchChart() {
  const ctx = document.getElementById('branchChart').getContext('2d');
  
  branchChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: dashboardData.branchData.map(item => `${item.branch}\n(${item.city})`),
      datasets: [{
        label: 'Revenue ($)',
        data: dashboardData.branchData.map(item => item.revenue),
        backgroundColor: chartColors.slice(0, 3),
        borderColor: chartColors.slice(0, 3).map(color => color + '80'),
        borderWidth: 1,
        borderRadius: 6,
        borderSkipped: false,
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      interaction: {
        intersect: false,
        mode: 'index'
      },
      plugins: {
        legend: {
          display: false
        },
        tooltip: {
          enabled: true,
          backgroundColor: 'rgba(0, 0, 0, 0.9)',
          titleColor: '#fff',
          bodyColor: '#fff',
          borderColor: '#1FB8CD',
          borderWidth: 2,
          cornerRadius: 8,
          displayColors: true,
          callbacks: {
            title: function(context) {
              const branch = dashboardData.branchData[context[0].dataIndex];
              return `${branch.branch} - ${branch.city}`;
            },
            label: function(context) {
              const branch = dashboardData.branchData[context.dataIndex];
              return [
                `Revenue: $${context.raw.toLocaleString()}`,
                `Transactions: ${branch.transactions}`,
                `Avg per Transaction: $${(context.raw / branch.transactions).toFixed(2)}`
              ];
            }
          }
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          ticks: {
            callback: function(value) {
              return '$' + (value / 1000).toFixed(0) + 'K';
            },
            color: '#626C71'
          },
          grid: {
            color: 'rgba(98, 108, 113, 0.1)'
          }
        },
        x: {
          ticks: {
            color: '#626C71',
            maxRotation: 0
          },
          grid: {
            display: false
          }
        }
      },
      onClick: function(event, elements) {
        if (elements.length > 0) {
          const index = elements[0].index;
          const branch = dashboardData.branchData[index];
          showBranchDetails(branch);
        }
      },
      onHover: function(event, elements) {
        event.native.target.style.cursor = elements.length > 0 ? 'pointer' : 'default';
      }
    }
  });
}

// Product Line Performance Chart
function initializeProductChart() {
  const ctx = document.getElementById('productChart').getContext('2d');
  
  productChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: dashboardData.productData.map(item => item.category),
      datasets: [{
        data: dashboardData.productData.map(item => item.revenue),
        backgroundColor: chartColors.slice(0, 6),
        borderColor: '#fff',
        borderWidth: 2,
        hoverBorderWidth: 4,
        hoverOffset: 10
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      interaction: {
        intersect: false
      },
      plugins: {
        legend: {
          position: 'right',
          labels: {
            usePointStyle: true,
            padding: 15,
            color: '#626C71',
            font: {
              size: 12
            }
          }
        },
        tooltip: {
          enabled: true,
          backgroundColor: 'rgba(0, 0, 0, 0.9)',
          titleColor: '#fff',
          bodyColor: '#fff',
          borderColor: '#1FB8CD',
          borderWidth: 2,
          cornerRadius: 8,
          displayColors: true,
          callbacks: {
            title: function(context) {
              return context[0].label;
            },
            label: function(context) {
              const product = dashboardData.productData[context.dataIndex];
              const total = dashboardData.productData.reduce((sum, p) => sum + p.revenue, 0);
              const percentage = ((context.raw / total) * 100).toFixed(1);
              return [
                `Revenue: $${context.raw.toLocaleString()}`,
                `Percentage: ${percentage}%`,
                `Transactions: ${product.transactions}`,
                `Rating: ${product.rating}/10`
              ];
            }
          }
        }
      },
      onClick: function(event, elements) {
        if (elements.length > 0) {
          const index = elements[0].index;
          const product = dashboardData.productData[index];
          showProductDetails(product);
        }
      },
      onHover: function(event, elements) {
        event.native.target.style.cursor = elements.length > 0 ? 'pointer' : 'default';
      }
    }
  });
}

// Monthly Sales Trend Chart
function initializeMonthlyChart() {
  const ctx = document.getElementById('monthlyChart').getContext('2d');
  
  monthlyChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: dashboardData.monthlyData.map(item => item.month),
      datasets: [{
        label: 'Monthly Revenue',
        data: dashboardData.monthlyData.map(item => item.revenue),
        borderColor: chartColors[0],
        backgroundColor: chartColors[0] + '20',
        borderWidth: 3,
        fill: true,
        tension: 0.4,
        pointBackgroundColor: chartColors[0],
        pointBorderColor: '#fff',
        pointBorderWidth: 2,
        pointRadius: 6,
        pointHoverRadius: 10,
        pointHoverBackgroundColor: chartColors[0],
        pointHoverBorderColor: '#fff',
        pointHoverBorderWidth: 3
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      interaction: {
        intersect: false,
        mode: 'index'
      },
      plugins: {
        legend: {
          display: false
        },
        tooltip: {
          enabled: true,
          backgroundColor: 'rgba(0, 0, 0, 0.9)',
          titleColor: '#fff',
          bodyColor: '#fff',
          borderColor: '#1FB8CD',
          borderWidth: 2,
          cornerRadius: 8,
          displayColors: false,
          callbacks: {
            title: function(context) {
              return `${context[0].label} 2024`;
            },
            label: function(context) {
              const month = dashboardData.monthlyData[context.dataIndex];
              return [
                `Revenue: $${context.raw.toLocaleString()}`,
                `Transactions: ${month.transactions}`,
                `Avg per Transaction: $${(context.raw / month.transactions).toFixed(2)}`
              ];
            }
          }
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          ticks: {
            callback: function(value) {
              return '$' + (value / 1000).toFixed(0) + 'K';
            },
            color: '#626C71'
          },
          grid: {
            color: 'rgba(98, 108, 113, 0.1)'
          }
        },
        x: {
          ticks: {
            color: '#626C71'
          },
          grid: {
            color: 'rgba(98, 108, 113, 0.1)'
          }
        }
      }
    }
  });
}

// Payment Methods Chart
function initializePaymentChart() {
  const ctx = document.getElementById('paymentChart').getContext('2d');
  
  paymentChart = new Chart(ctx, {
    type: 'pie',
    data: {
      labels: dashboardData.paymentData.map(item => item.method),
      datasets: [{
        data: dashboardData.paymentData.map(item => item.percentage),
        backgroundColor: chartColors.slice(0, 3),
        borderColor: '#fff',
        borderWidth: 2,
        hoverBorderWidth: 4,
        hoverOffset: 8
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      interaction: {
        intersect: false
      },
      plugins: {
        legend: {
          position: 'bottom',
          labels: {
            usePointStyle: true,
            padding: 15,
            color: '#626C71',
            font: {
              size: 12
            }
          }
        },
        tooltip: {
          enabled: true,
          backgroundColor: 'rgba(0, 0, 0, 0.9)',
          titleColor: '#fff',
          bodyColor: '#fff',
          borderColor: '#1FB8CD',
          borderWidth: 2,
          cornerRadius: 8,
          displayColors: true,
          callbacks: {
            title: function(context) {
              return context[0].label;
            },
            label: function(context) {
              const payment = dashboardData.paymentData[context.dataIndex];
              return [
                `Percentage: ${context.raw}%`,
                `Revenue: $${payment.revenue.toLocaleString()}`
              ];
            }
          }
        }
      }
    }
  });
}

// Event Listeners
function attachEventListeners() {
  // Filter change handlers
  document.getElementById('branchFilter').addEventListener('change', handleFilterChange);
  document.getElementById('productFilter').addEventListener('change', handleFilterChange);
  document.getElementById('customerFilter').addEventListener('change', handleFilterChange);
  document.getElementById('dateFilter').addEventListener('change', handleFilterChange);
  
  // Button handlers
  document.getElementById('refreshBtn').addEventListener('click', refreshDashboard);
  document.getElementById('exportBtn').addEventListener('click', exportData);
  document.getElementById('printBtn').addEventListener('click', printDashboard);
}

// Handle filter changes
function handleFilterChange() {
  const filters = {
    branch: document.getElementById('branchFilter').value,
    product: document.getElementById('productFilter').value,
    customer: document.getElementById('customerFilter').value,
    date: document.getElementById('dateFilter').value
  };
  
  applyFilters(filters);
  updateKPIs(filters);
}

// Apply filters to charts
function applyFilters(filters) {
  showFilterFeedback(filters);
}

// Show filter feedback
function showFilterFeedback(filters) {
  const activeFilters = Object.entries(filters).filter(([key, value]) => value !== 'all');
  
  if (activeFilters.length > 0) {
    document.body.classList.add('filters-active');
  } else {
    document.body.classList.remove('filters-active');
  }
}

// Update KPIs based on filters
function updateKPIs(filters) {
  if (filters.branch === 'B') {
    document.getElementById('totalRevenue').textContent = '$142,281.48';
    document.getElementById('totalTransactions').textContent = '429';
    document.getElementById('totalGrossIncome').textContent = '$47,013.29';
  } else if (filters.branch === 'C') {
    document.getElementById('totalRevenue').textContent = '$123,299.25';
    document.getElementById('totalTransactions').textContent = '387';
    document.getElementById('totalGrossIncome').textContent = '$40,769.86';
  } else if (filters.branch === 'A') {
    document.getElementById('totalRevenue').textContent = '$119,941.29';
    document.getElementById('totalTransactions').textContent = '384';
    document.getElementById('totalGrossIncome').textContent = '$39,641.10';
  } else {
    // Reset to original values
    document.getElementById('totalRevenue').textContent = dashboardData.kpis.totalRevenue;
    document.getElementById('totalTransactions').textContent = dashboardData.kpis.totalTransactions;
    document.getElementById('totalGrossIncome').textContent = dashboardData.kpis.totalGrossIncome;
  }
}

// Show branch details
function showBranchDetails(branch) {
  const modal = createModal('Branch Details', `
    <div style="text-align: left; line-height: 1.6;">
      <p><strong>Location:</strong> ${branch.city}</p>
      <p><strong>Revenue:</strong> $${branch.revenue.toLocaleString()}</p>
      <p><strong>Transactions:</strong> ${branch.transactions}</p>
      <p><strong>Average per Transaction:</strong> $${(branch.revenue / branch.transactions).toFixed(2)}</p>
      <p><strong>Performance:</strong> ${branch.branch === 'Branch B' ? 'Top Performer' : branch.branch === 'Branch C' ? 'Above Average' : 'Needs Improvement'}</p>
    </div>
  `);
  document.body.appendChild(modal);
}

// Show product details
function showProductDetails(product) {
  const total = dashboardData.productData.reduce((sum, p) => sum + p.revenue, 0);
  const percentage = ((product.revenue / total) * 100).toFixed(1);
  
  const modal = createModal('Product Line Details', `
    <div style="text-align: left; line-height: 1.6;">
      <p><strong>Category:</strong> ${product.category}</p>
      <p><strong>Revenue:</strong> $${product.revenue.toLocaleString()}</p>
      <p><strong>Market Share:</strong> ${percentage}%</p>
      <p><strong>Transactions:</strong> ${product.transactions}</p>
      <p><strong>Average Rating:</strong> ${product.rating}/10</p>
      <p><strong>Performance:</strong> ${product.rating >= 7 ? 'Excellent' : product.rating >= 6.9 ? 'Good' : 'Fair'}</p>
    </div>
  `);
  document.body.appendChild(modal);
}

// Create modal dialog
function createModal(title, content) {
  const modal = document.createElement('div');
  modal.className = 'modal-overlay';
  modal.innerHTML = `
    <div class="modal-content">
      <div class="modal-header">
        <h3>${title}</h3>
        <button class="modal-close">&times;</button>
      </div>
      <div class="modal-body">
        ${content}
      </div>
    </div>
  `;
  
  // Close modal handlers
  modal.querySelector('.modal-close').onclick = () => document.body.removeChild(modal);
  modal.onclick = (e) => {
    if (e.target === modal) document.body.removeChild(modal);
  };
  
  // Add styles if not already present
  if (!document.querySelector('#modal-styles')) {
    const styles = document.createElement('style');
    styles.id = 'modal-styles';
    styles.textContent = `
      .modal-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 1000;
      }
      .modal-content {
        background: var(--color-surface);
        border-radius: var(--radius-lg);
        max-width: 500px;
        width: 90%;
        max-height: 80%;
        overflow: auto;
        box-shadow: var(--shadow-lg);
      }
      .modal-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: var(--space-20);
        border-bottom: 1px solid var(--color-border);
      }
      .modal-header h3 {
        margin: 0;
        color: var(--color-text);
      }
      .modal-close {
        background: none;
        border: none;
        font-size: 24px;
        cursor: pointer;
        color: var(--color-text-secondary);
        padding: 0;
        width: 30px;
        height: 30px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
      }
      .modal-close:hover {
        background: var(--color-secondary);
        color: var(--color-text);
      }
      .modal-body {
        padding: var(--space-20);
      }
    `;
    document.head.appendChild(styles);
  }
  
  return modal;
}

// Refresh dashboard
function refreshDashboard() {
  const btn = document.getElementById('refreshBtn');
  btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Refreshing...';
  btn.disabled = true;
  
  setTimeout(() => {
    // Reset filters
    document.getElementById('branchFilter').value = 'all';
    document.getElementById('productFilter').value = 'all';
    document.getElementById('customerFilter').value = 'all';
    document.getElementById('dateFilter').value = 'all';
    
    // Reset KPIs
    document.getElementById('totalRevenue').textContent = dashboardData.kpis.totalRevenue;
    document.getElementById('totalTransactions').textContent = dashboardData.kpis.totalTransactions;
    document.getElementById('totalGrossIncome').textContent = dashboardData.kpis.totalGrossIncome;
    
    // Update charts
    branchChart.update();
    productChart.update();
    monthlyChart.update();
    paymentChart.update();
    
    // Update timestamp
    updateLastRefreshed();
    
    // Remove loading state
    btn.innerHTML = '<i class="fas fa-sync-alt"></i> Refresh';
    btn.disabled = false;
    
    // Remove filter indicators
    document.body.classList.remove('filters-active');
  }, 1500);
}

// Export data
function exportData() {
  let csvContent = "data:text/csv;charset=utf-8,";
  
  csvContent += "Category,Value\n";
  csvContent += `Total Revenue,${dashboardData.kpis.totalRevenue}\n`;
  csvContent += `Total Gross Income,${dashboardData.kpis.totalGrossIncome}\n`;
  csvContent += `Total Transactions,${dashboardData.kpis.totalTransactions}\n`;
  
  csvContent += "\nBranch Performance\n";
  csvContent += "Branch,City,Revenue,Transactions\n";
  dashboardData.branchData.forEach(branch => {
    csvContent += `${branch.branch},${branch.city},${branch.revenue},${branch.transactions}\n`;
  });
  
  const encodedUri = encodeURI(csvContent);
  const link = document.createElement("a");
  link.setAttribute("href", encodedUri);
  link.setAttribute("download", "supermarket_sales_dashboard.csv");
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  
  // Show feedback
  const btn = document.getElementById('exportBtn');
  const originalText = btn.innerHTML;
  btn.innerHTML = '<i class="fas fa-check"></i> Exported!';
  setTimeout(() => {
    btn.innerHTML = originalText;
  }, 2000);
}

// Print dashboard
function printDashboard() {
  window.print();
}

// Update last refreshed timestamp
function updateLastRefreshed() {
  const now = new Date();
  const timestamp = now.toLocaleString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    hour12: true
  });
  document.getElementById('lastUpdated').textContent = timestamp;
}

// Handle window resize for chart responsiveness
window.addEventListener('resize', function() {
  if (branchChart) branchChart.resize();
  if (productChart) productChart.resize();
  if (monthlyChart) monthlyChart.resize();
  if (paymentChart) paymentChart.resize();
});