# from aiogram.dispatcher.filters import Text
import os
import time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from remove_bg import remove_background

def bot_start(token):
    bot = Bot(token=token)
    dp = Dispatcher(bot, storage=MemoryStorage())

    @dp.message_handler(commands='start')
    async def start(message: types.Message):
        await message.answer('Привет')

    @dp.message_handler(content_types=['document'])
    async def document(message: types.Message):
        file_type = message.document.mime_type
        if file_type == 'image/jpeg' or file_type == 'image/png':
            document_id = message.document.file_id
            file_name = message.document.file_name
            file_info = await bot.get_file(document_id)
            input_path = './original_photos/' + file_name
            await bot.download_file(file_info.file_path, input_path)
            output_path = None
            if os.path.exists(input_path):
                new_file_name = await remove_background(file_name)
                output_path = './no_bg_photos/' + new_file_name
                os.remove(input_path)
            else:
                await message.answer('Не удалось сохранить ваш файл')
            if os.path.exists(output_path):
                with open(output_path, 'rb') as f:
                    await bot.send_document(message.chat.id, f)
                os.remove(output_path)
            else:
                await message.answer('Не удалось убрать фон в вашем изображении')
        else:
            await message.answer('Неверный формат файла')

    executor.start_polling(dp)
