import reflex as rx

config = rx.Config(
    app_name="Fraud_",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)