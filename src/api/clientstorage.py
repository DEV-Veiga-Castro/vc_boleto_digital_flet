import os
import base64

import flet as ft
import flet_secure_storage as fss

import asyncio

class ClientStorage:

    def __init__(self, prefs: ft.SharedPreferences = ft.SharedPreferences):
        self.prefs = prefs
        self.fallback_storage = {}
        self.use_fallback = False

    async def set_token(self, access_token: str, refresh_token: str) -> None:
        if self.use_fallback:
            self.fallback_storage["access_token"] = access_token
            return
        
        try:
            await asyncio.wait_for(
                fut=await self.prefs.set("acess_token", access_token),
                timeout=2.0
            )

            await asyncio.wait_for(
                fut=await self.prefs.set("refresh_token", refresh_token),
                timeout=2.0
            )

        except (asyncio.TimeoutError, RuntimeError, Exception) as e:
            print(f"[Storage Warning] Timeout/Erro ao salvar '{"tokens"}'. Mudando para o modo Fallback. Erro: {e}.")
            self.use_fallback = True
            self.fallback_storage["access_token"] = access_token
            self.fallback_storage["refresh_token"] = refresh_token

    async def get_access_token(self) -> str:
        if self.use_fallback:
            return self.fallback_storage.get("access_token", None)
        
        try:
            has_key = await asyncio.wait_for(
                await self.prefs.contains_key("access_token"),
                timeout=2.0
            )

            if has_key:
                return await self.prefs.get("access_token")
            
            return None
        
        except (asyncio.TimeoutError, RuntimeError, Exception) as e:
            print(f"[Storage Warning] Timeout/Erro ao ler '{"access_token ", e}'. Buscando da memória local.")
            self.use_fallback = True
            return self.fallback_storage.get("access_token", None)

    async def get_refresh_token(self) -> str:
        if self.use_fallback:
            return self.fallback_storage.get("refresh_token", None)
        
        try:
            has_key = await asyncio.wait_for(
                await self.prefs.contains_key("refresh_token"),
                timeout=2.0
            )

            if has_key:
                return await self.prefs.get("refresh_token")
            
            return None
        
        except (asyncio.TimeoutError, RuntimeError, Exception) as e:
            print(f"[Storage Warning] Timeout/Erro ao ler '{"refresh_token ", e}'. Buscando da memória local.")
            self.use_fallback = True
            return self.fallback_storage.get("refresh_token", None)

    async def clear_token(self) -> None:
        if self.use_fallback:
            self.fallback_storage.pop("access_token")
            self.fallback_storage.pop("refresh_token")
            return
        
        try:
            await asyncio.wait_for(
                fut=[
                    self.prefs.remove("access_token"),
                    self.prefs.remove("refresh_token")
                ],
                timeout=2.0
            )
        except (asyncio.TimeoutError, RuntimeError, Exception) as e:
            print(f"[Storage Warning] Timeout/Erro na exclusão das chaves. {e}")

    async def is_authenticated(self) -> bool:
        access_token = await self.get_access_token()
        return access_token is not None