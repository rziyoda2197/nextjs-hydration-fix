import os
import json

def fix_hydration_error(project_path):
    # Next.js proyektini topish
    nextjs_project_path = os.path.join(project_path, 'pages')

    # HydrateError ni tuzatish uchun qaror qabul qilish
    if os.path.exists(nextjs_project_path):
        # pages dizini ichidagi fayllarni o'qish
        for filename in os.listdir(nextjs_project_path):
            filepath = os.path.join(nextjs_project_path, filename)

            # Foydalanuvchi fayli o'qish
            with open(filepath, 'r') as file:
                content = file.read()

            # Foydalanuvchi faylini yangilash
            content = content.replace('import dynamic from "next/dynamic";', 'import dynamic from "next/dynamic";\nimport { AppProps } from "next/app";')

            # Yangilangan foydalanuvchi faylini yozish
            with open(filepath, 'w') as file:
                file.write(content)

            # Foydalanuvchi faylini yangilash
            content = content.replace('export default function App({ Component, pageProps }: AppProps) {', 'export default function App({ Component, pageProps }: AppProps) {\n  return <Component {...pageProps} />;')

            # Yangilangan foydalanuvchi faylini yozish
            with open(filepath, 'w') as file:
                file.write(content)

# Proyekt pathni kiritish
project_path = input("Proyekt pathni kiriting: ")

# HydrateError ni tuzatish
fix_hydration_error(project_path)
