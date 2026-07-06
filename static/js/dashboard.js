document.addEventListener("DOMContentLoaded", () => {
    const userChart = document.getElementById("userChart");
    if (userChart && window.Chart) {
        new Chart(userChart, {
            type: "doughnut",
            data: {
                labels: ["Lost", "Found", "Claims"],
                datasets: [{
                    data: [
                        Number(userChart.dataset.lost || 0),
                        Number(userChart.dataset.found || 0),
                        Number(userChart.dataset.matches || 0),
                    ],
                    backgroundColor: ["#ef4444", "#10b981", "#7c3aed"],
                    borderWidth: 0,
                }],
            },
            options: {
                plugins: { legend: { position: "bottom" } },
                cutout: "64%",
            },
        });
    }

    const adminChart = document.getElementById("adminChart");
    if (adminChart && window.Chart) {
        const categories = JSON.parse(adminChart.dataset.categories || "[]");
        new Chart(adminChart, {
            type: "bar",
            data: {
                labels: categories.map((row) => row.category),
                datasets: [
                    {
                        label: "Lost",
                        data: categories.map((row) => row.lost_count),
                        backgroundColor: "#ef4444",
                        borderRadius: 8,
                    },
                    {
                        label: "Found",
                        data: categories.map((row) => row.found_count),
                        backgroundColor: "#10b981",
                        borderRadius: 8,
                    },
                ],
            },
            options: {
                responsive: true,
                scales: { y: { beginAtZero: true, ticks: { precision: 0 } } },
                plugins: { legend: { position: "bottom" } },
            },
        });
    }
});
