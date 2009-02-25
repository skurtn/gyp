{
  'includes': [
    '../build/common.gypi',
  ],
  'targets': [
    {
      'target_name': 'skia',
      'type': 'static_library',
      'sources': [
        'precompiled.cc',
        #'animator/SkAnimate.h',
        #'animator/SkAnimateActive.cpp',
        #'animator/SkAnimateActive.h',
        #'animator/SkAnimateBase.cpp',
        #'animator/SkAnimateBase.h',
        #'animator/SkAnimateField.cpp',
        #'animator/SkAnimateMaker.cpp',
        #'animator/SkAnimateMaker.h',
        #'animator/SkAnimateProperties.h',
        #'animator/SkAnimateSet.cpp',
        #'animator/SkAnimateSet.h',
        #'animator/SkAnimator.cpp',
        #'animator/SkAnimatorScript.cpp',
        #'animator/SkAnimatorScript.h',
        #'animator/SkAnimatorScript2.cpp',
        #'animator/SkAnimatorScript2.h',
        #'animator/SkBase64.cpp',
        #'animator/SkBase64.h',
        #'animator/SkBoundable.cpp',
        #'animator/SkBoundable.h',
        #'animator/SkBuildCondensedInfo.cpp',
        #'animator/SkCondensedDebug.cpp',
        #'animator/SkCondensedRelease.cpp',
        #'animator/SkDisplayable.cpp',
        #'animator/SkDisplayable.h',
        #'animator/SkDisplayAdd.cpp',
        #'animator/SkDisplayAdd.h',
        #'animator/SkDisplayApply.cpp',
        #'animator/SkDisplayApply.h',
        #'animator/SkDisplayBounds.cpp',
        #'animator/SkDisplayBounds.h',
        #'animator/SkDisplayEvent.cpp',
        #'animator/SkDisplayEvent.h',
        #'animator/SkDisplayEvents.cpp',
        #'animator/SkDisplayEvents.h',
        #'animator/SkDisplayInclude.cpp',
        #'animator/SkDisplayInclude.h',
        #'animator/SkDisplayInput.cpp',
        #'animator/SkDisplayInput.h',
        #'animator/SkDisplayList.cpp',
        #'animator/SkDisplayList.h',
        #'animator/SkDisplayMath.cpp',
        #'animator/SkDisplayMath.h',
        #'animator/SkDisplayMovie.cpp',
        #'animator/SkDisplayMovie.h',
        #'animator/SkDisplayNumber.cpp',
        #'animator/SkDisplayNumber.h',
        #'animator/SkDisplayPost.cpp',
        #'animator/SkDisplayPost.h',
        #'animator/SkDisplayRandom.cpp',
        #'animator/SkDisplayRandom.h',
        #'animator/SkDisplayScreenplay.cpp',
        #'animator/SkDisplayScreenplay.h',
        #'animator/SkDisplayType.cpp',
        #'animator/SkDisplayType.h',
        #'animator/SkDisplayTypes.cpp',
        #'animator/SkDisplayTypes.h',
        #'animator/SkDisplayXMLParser.cpp',
        #'animator/SkDisplayXMLParser.h',
        #'animator/SkDraw3D.cpp',
        #'animator/SkDraw3D.h',
        #'animator/SkDrawable.cpp',
        #'animator/SkDrawable.h',
        #'animator/SkDrawBitmap.cpp',
        #'animator/SkDrawBitmap.h',
        #'animator/SkDrawBlur.cpp',
        #'animator/SkDrawBlur.h',
        #'animator/SkDrawClip.cpp',
        #'animator/SkDrawClip.h',
        #'animator/SkDrawColor.cpp',
        #'animator/SkDrawColor.h',
        #'animator/SkDrawDash.cpp',
        #'animator/SkDrawDash.h',
        #'animator/SkDrawDiscrete.cpp',
        #'animator/SkDrawDiscrete.h',
        #'animator/SkDrawEmboss.cpp',
        #'animator/SkDrawEmboss.h',
        #'animator/SkDrawExtraPathEffect.cpp',
        #'animator/SkDrawFull.cpp',
        #'animator/SkDrawFull.h',
        #'animator/SkDrawGradient.cpp',
        #'animator/SkDrawGradient.h',
        #'animator/SkDrawGroup.cpp',
        #'animator/SkDrawGroup.h',
        #'animator/SkDrawLine.cpp',
        #'animator/SkDrawLine.h',
        #'animator/SkDrawMatrix.cpp',
        #'animator/SkDrawMatrix.h',
        #'animator/SkDrawOval.cpp',
        #'animator/SkDrawOval.h',
        #'animator/SkDrawPaint.cpp',
        #'animator/SkDrawPaint.h',
        #'animator/SkDrawPath.cpp',
        #'animator/SkDrawPath.h',
        #'animator/SkDrawPoint.cpp',
        #'animator/SkDrawPoint.h',
        #'animator/SkDrawRectangle.cpp',
        #'animator/SkDrawRectangle.h',
        #'animator/SkDrawSaveLayer.cpp',
        #'animator/SkDrawSaveLayer.h',
        #'animator/SkDrawShader.cpp',
        #'animator/SkDrawShader.h',
        #'animator/SkDrawText.cpp',
        #'animator/SkDrawText.h',
        #'animator/SkDrawTextBox.cpp',
        #'animator/SkDrawTextBox.h',
        #'animator/SkDrawTo.cpp',
        #'animator/SkDrawTo.h',
        #'animator/SkDrawTransparentShader.cpp',
        #'animator/SkDrawTransparentShader.h',
        #'animator/SkDump.cpp',
        #'animator/SkDump.h',
        #'animator/SkExtras.h',
        #'animator/SkGetCondensedInfo.cpp',
        #'animator/SkHitClear.cpp',
        #'animator/SkHitClear.h',
        #'animator/SkHitTest.cpp',
        #'animator/SkHitTest.h',
        #'animator/SkIntArray.h',
        #'animator/SkMatrixParts.cpp',
        #'animator/SkMatrixParts.h',
        #'animator/SkMemberInfo.cpp',
        #'animator/SkMemberInfo.h',
        #'animator/SkOpArray.cpp',
        #'animator/SkOpArray.h',
        #'animator/SkOperand.h',
        #'animator/SkOperand2.h',
        #'animator/SkOperandInterpolator.h',
        #'animator/SkOperandIterpolator.cpp',
        #'animator/SkPaintParts.cpp',
        #'animator/SkPaintParts.h',
        #'animator/SkPathParts.cpp',
        #'animator/SkPathParts.h',
        #'animator/SkPostParts.cpp',
        #'animator/SkPostParts.h',
        #'animator/SkScript.cpp',
        #'animator/SkScript.h',
        #'animator/SkScript2.h',
        #'animator/SkScriptCallBack.h',
        #'animator/SkScriptDecompile.cpp',
        #'animator/SkScriptRuntime.cpp',
        #'animator/SkScriptRuntime.h',
        #'animator/SkScriptTokenizer.cpp',
        #'animator/SkSnapshot.cpp',
        #'animator/SkSnapshot.h',
        #'animator/SkSVGPath.cpp',
        #'animator/SkTDArray_Experimental.h',
        #'animator/SkTextOnPath.cpp',
        #'animator/SkTextOnPath.h',
        #'animator/SkTextToPath.cpp',
        #'animator/SkTextToPath.h',
        'animator/SkTime.cpp',
        #'animator/SkTypedArray.cpp',
        #'animator/SkTypedArray.h',
        #'animator/SkXMLAnimatorWriter.cpp',
        #'animator/SkXMLAnimatorWriter.h',
        'corecg/Sk64.cpp',
        'corecg/SkBuffer.cpp',
        'corecg/SkChunkAlloc.cpp',
        'corecg/SkCordic.cpp',
        'corecg/SkCordic.h',
        'corecg/SkDebug.cpp',
        'corecg/SkDebug_stdio.cpp',
        'corecg/SkFloat.cpp',
        'corecg/SkFloat.h',
        'corecg/SkFloatBits.cpp',
        'corecg/SkFloatBits.h',
        'corecg/SkInterpolator.cpp',
        'corecg/SkMath.cpp',
        'corecg/SkMatrix.cpp',
        'corecg/SkMemory_stdlib.cpp',
        'corecg/SkPageFlipper.cpp',
        'corecg/SkPoint.cpp',
        'corecg/SkRect.cpp',
        'corecg/SkRegion.cpp',
        'corecg/SkRegionPriv.h',
        'corecg/SkSinTable.h',
        'corecg/SkTSort.h',
        'effects/Sk1DPathEffect.cpp',
        'effects/Sk2DPathEffect.cpp',
        'effects/SkAvoidXfermode.cpp',
        'effects/SkBlurDrawLooper.cpp',
        'effects/SkBlurMask.cpp',
        'effects/SkBlurMask.h',
        'effects/SkBlurMaskFilter.cpp',
        'effects/SkCamera.cpp',
        'effects/SkColorFilters.cpp',
        'effects/SkColorMatrix.cpp',
        'effects/SkColorMatrixFilter.cpp',
        'effects/SkCornerPathEffect.cpp',
        'effects/SkCullPoints.cpp',
        'effects/SkDashPathEffect.cpp',
        'effects/SkDiscretePathEffect.cpp',
        'effects/SkEmbossMask.cpp',
        'effects/SkEmbossMask.h',
        'effects/SkEmbossMask_Table.h',
        'effects/SkEmbossMaskFilter.cpp',
        'effects/SkGradientShader.cpp',
        'effects/SkKernel33MaskFilter.cpp',
        #'effects/SkLayerDrawLooper.cpp',
        'effects/SkLayerRasterizer.cpp',
        #'effects/SkNinePatch.cpp',
        'effects/SkPaintFlagsDrawFilter.cpp',
        'effects/SkPixelXorXfermode.cpp',
        'effects/SkRadialGradient_Table.h',
        'effects/SkShaderExtras.cpp',
        'effects/SkTransparentShader.cpp',
        'effects/SkUnitMappers.cpp',
        'ext/bitmap_platform_device.h',
        'ext/bitmap_platform_device_linux.cc',
        'ext/bitmap_platform_device_linux.h',
        'ext/bitmap_platform_device_mac.cc',
        'ext/bitmap_platform_device_mac.h',
        'ext/bitmap_platform_device_win.cc',
        'ext/bitmap_platform_device_win.h',
        'ext/convolver.cc',
        'ext/convolver.h',
        'ext/GdkSkia.cc',
        'ext/GdkSkia.h',
        'ext/google_logging.cc',
        'ext/image_operations.cc',
        'ext/image_operations.h',
        'ext/platform_canvas.h',
        'ext/platform_canvas_linux.cc',
        'ext/platform_canvas_linux.h',
        'ext/platform_canvas_mac.cc',
        'ext/platform_canvas_mac.h',
        'ext/platform_canvas_win.cc',
        'ext/platform_canvas_win.h',
        'ext/platform_device.h',
        'ext/platform_device_linux.cc',
        'ext/platform_device_linux.h',
        'ext/platform_device_mac.cc',
        'ext/platform_device_mac.h',
        'ext/platform_device_win.cc',
        'ext/platform_device_win.h',
        'ext/skia_utils.cc',
        'ext/skia_utils.h',
        'ext/skia_utils_mac.cc',
        'ext/skia_utils_mac.h',
        'ext/skia_utils_win.cc',
        'ext/skia_utils_win.h',
        'ext/vector_canvas.cc',
        'ext/vector_canvas.h',
        'ext/vector_device.cc',
        'ext/vector_device.h',
        #'gl/SkGL.cpp',
        #'gl/SkGL.h',
        #'gl/SkGLCanvas.cpp',
        #'gl/SkGLDevice.cpp',
        #'gl/SkGLDevice.h',
        #'gl/SkGLDevice_FBO.cpp',
        #'gl/SkGLDevice_FBO.h',
        #'gl/SkGLDevice_SWLayer.cpp',
        #'gl/SkGLDevice_SWLayer.h',
        #'gl/SkGLTextCache.cpp',
        #'gl/SkGLTextCache.h',
        #'gl/SkTextureCache.cpp',
        #'gl/SkTextureCache.h',
        #'images/bmpdecoderhelper.cpp',
        #'images/bmpdecoderhelper.h',
        #'images/fpdfemb.h',
        #'images/fpdfemb_ext.h',
        #'images/SkBitmap_RLEPixels.h',
        #'images/SkCreateRLEPixelRef.cpp',
        #'images/SkFDStream.cpp',
        #'images/SkFlipPixelRef.cpp',
        'images/SkImageDecoder.cpp',
        #'images/SkImageDecoder_fpdfemb.cpp',
        #'images/SkImageDecoder_libbmp.cpp',
        #'images/SkImageDecoder_libgif.cpp',
        #'images/SkImageDecoder_libico.cpp',
        #'images/SkImageDecoder_libjpeg.cpp',
        #'images/SkImageDecoder_libpng.cpp',
        #'images/SkImageDecoder_libpvjpeg.cpp',
        #'images/SkImageDecoder_wbmp.cpp',
        'images/SkImageRef.cpp',
        #'images/SkImageRef_GlobalPool.cpp',
        #'images/SkImageRefPool.cpp',
        #'images/SkImageRefPool.h',
        'images/SkMMapStream.cpp',
        #'images/SkMovie.cpp',
        #'images/SkMovie_gif.cpp',
        #'images/SkScaledBitmapSampler.cpp',
        #'images/SkScaledBitmapSampler.h',
        'images/SkStream.cpp',
        'include/corecg/Sk64.h',
        'include/corecg/SkBuffer.h',
        'include/corecg/SkChunkAlloc.h',
        'include/corecg/SkEndian.h',
        'include/corecg/SkFDot6.h',
        'include/corecg/SkFixed.h',
        'include/corecg/SkFloatBits.h',
        'include/corecg/SkFloatingPoint.h',
        'include/corecg/SkInterpolator.h',
        'include/corecg/SkMath.h',
        'include/corecg/SkMatrix.h',
        'include/corecg/SkPageFlipper.h',
        'include/corecg/SkPerspIter.h',
        'include/corecg/SkPoint.h',
        'include/corecg/SkPostConfig.h',
        'include/corecg/SkPreConfig.h',
        'include/corecg/SkRandom.h',
        'include/corecg/SkRect.h',
        'include/corecg/SkRegion.h',
        'include/corecg/SkScalar.h',
        'include/corecg/SkScalarCompare.h',
        'include/corecg/SkTemplates.h',
        'include/corecg/SkThread.h',
        'include/corecg/SkThread_platform.h',
        'include/corecg/SkTSearch.h',
        'include/corecg/SkTypes.h',
        'include/corecg/SkUserConfig.h',
        'include/Sk1DPathEffect.h',
        'include/Sk2DPathEffect.h',
        'include/SkAnimator.h',
        'include/SkAnimatorView.h',
        'include/SkApplication.h',
        'include/SkAvoidXfermode.h',
        'include/SkBGViewArtist.h',
        'include/SkBitmap.h',
        'include/SkBlurDrawLooper.h',
        'include/SkBlurMaskFilter.h',
        'include/SkBML_WXMLParser.h',
        'include/SkBML_XMLParser.h',
        'include/SkBorderView.h',
        'include/SkBounder.h',
        'include/SkCamera.h',
        'include/SkCanvas.h',
        'include/SkColor.h',
        'include/SkColorFilter.h',
        'include/SkColorMatrix.h',
        'include/SkColorMatrixFilter.h',
        'include/SkColorPriv.h',
        'include/SkColorShader.h',
        'include/SkCornerPathEffect.h',
        'include/SkCullPoints.h',
        'include/SkDashPathEffect.h',
        'include/SkDeque.h',
        'include/SkDescriptor.h',
        'include/SkDevice.h',
        'include/SkDiscretePathEffect.h',
        'include/SkDither.h',
        'include/SkDOM.h',
        'include/SkDraw.h',
        'include/SkDrawExtraPathEffect.h',
        'include/SkDrawFilter.h',
        'include/SkDrawLooper.h',
        'include/SkEmbossMaskFilter.h',
        'include/SkEvent.h',
        'include/SkEventSink.h',
        'include/SkFlattenable.h',
        'include/SkFlipPixelRef.h',
        'include/SkFontCodec.h',
        'include/SkFontHost.h',
        'include/SkGLCanvas.h',
        'include/SkGlobals.h',
        'include/SkGradientShader.h',
        'include/SkGraphics.h',
        'include/SkImageDecoder.h',
        'include/SkImageRef.h',
        'include/SkImageRef_GlobalPool.h',
        'include/SkImageView.h',
        'include/SkJS.h',
        'include/SkKernel33MaskFilter.h',
        'include/SkKey.h',
        'include/SkLayerDrawLooper.h',
        'include/SkLayerRasterizer.h',
        'include/SkMallocPixelRef.h',
        'include/SkMask.h',
        'include/SkMaskFilter.h',
        'include/SkMetaData.h',
        'include/SkMMapStream.h',
        'include/SkMovie.h',
        'include/SkNinePatch.h',
        'include/SkOSFile.h',
        'include/SkOSMenu.h',
        'include/SkOSSound.h',
        'include/SkOSWindow_Mac.h',
        'include/SkOSWindow_Unix.h',
        'include/SkOSWindow_Win.h',
        'include/SkOSWindow_wxwidgets.h',
        'include/SkPackBits.h',
        'include/SkPaint.h',
        'include/SkPaintFlagsDrawFilter.h',
        'include/SkParse.h',
        'include/SkParsePaint.h',
        'include/SkPath.h',
        'include/SkPathEffect.h',
        'include/SkPathMeasure.h',
        'include/SkPicture.h',
        'include/SkPixelRef.h',
        'include/SkPixelXorXfermode.h',
        'include/SkPorterDuff.h',
        'include/SkProgressBarView.h',
        'include/SkPtrRecorder.h',
        'include/SkRasterizer.h',
        'include/SkReader32.h',
        'include/SkRefCnt.h',
        'include/SkScalerContext.h',
        'include/SkScrollBarView.h',
        'include/SkShader.h',
        'include/SkShaderExtras.h',
        'include/SkStackViewLayout.h',
        'include/SkStream.h',
        'include/SkStream_Win.h',
        'include/SkString.h',
        'include/SkStroke.h',
        'include/SkSVGAttribute.h',
        'include/SkSVGBase.h',
        'include/SkSVGPaintState.h',
        'include/SkSVGParser.h',
        'include/SkSVGTypes.h',
        'include/SkSystemEventTypes.h',
        'include/SkTDArray.h',
        'include/SkTDict.h',
        'include/SkTDStack.h',
        'include/SkTextBox.h',
        'include/SkTime.h',
        'include/SkTransparentShader.h',
        'include/SkTypeface.h',
        'include/SkUnitMapper.h',
        'include/SkUnitMappers.h',
        'include/SkUnPreMultiply.h',
        'include/SkUtils.h',
        'include/SkView.h',
        'include/SkViewInflate.h',
        'include/SkWidget.h',
        'include/SkWidgetViews.h',
        'include/SkWindow.h',
        'include/SkWriter32.h',
        'include/SkXfermode.h',
        'include/SkXMLParser.h',
        'include/SkXMLWriter.h',
        'picture/SkPathHeap.cpp',
        'picture/SkPathHeap.h',
        'picture/SkPicture.cpp',
        'picture/SkPictureFlat.cpp',
        'picture/SkPictureFlat.h',
        'picture/SkPicturePlayback.cpp',
        'picture/SkPicturePlayback.h',
        'picture/SkPictureRecord.cpp',
        'picture/SkPictureRecord.h',
        'ports/sk_predefined_gamma.h',
        #'ports/SkFontHost_android.cpp',
        #'ports/SkFontHost_ascender.cpp',
        'ports/SkFontHost_fontconfig.cpp',
        #'ports/SkFontHost_FONTPATH.cpp',
        'ports/SkFontHost_FreeType.cpp',
        #'ports/SkFontHost_gamma.cpp',
        'ports/SkFontHost_gamma_none.cpp',
        #'ports/SkFontHost_linux.cpp',
        #'ports/SkFontHost_mac.cpp',
        'ports/SkFontHost_none.cpp',
        'ports/SkFontHost_TrueType_Tables.cpp',
        #'ports/SkFontHost_win.cpp',
        'ports/SkGlobals_global.cpp',
        'ports/SkImageDecoder_Factory.cpp',
        #'ports/SkImageRef_ashmem.cpp',
        #'ports/SkImageRef_ashmem.h',
        #'ports/SkOSEvent_android.cpp',
        #'ports/SkOSEvent_dummy.cpp',
        'ports/SkOSFile_stdio.cpp',
        #'ports/SkThread_none.cpp',
        'ports/SkThread_pthread.cpp',
        'ports/SkThread_win.cpp',
        'ports/SkTime_Unix.cpp',
        #'ports/SkXMLParser_empty.cpp',
        #'ports/SkXMLParser_expat.cpp',
        #'ports/SkXMLParser_tinyxml.cpp',
        #'ports/SkXMLPullParser_expat.cpp',
        'sgl/ARGB32_Clamp_Bilinear_BitmapShader.h',
        'sgl/SkAlphaRuns.cpp',
        'sgl/SkAntiRun.h',
        'sgl/SkAutoKern.h',
        'sgl/SkBitmap.cpp',
        #'sgl/SkBitmap_scroll.cpp',
        'sgl/SkBitmapProcShader.cpp',
        'sgl/SkBitmapProcShader.h',
        'sgl/SkBitmapProcState.cpp',
        'sgl/SkBitmapProcState.h',
        'sgl/SkBitmapProcState_matrix.h',
        'sgl/SkBitmapProcState_matrixProcs.cpp',
        'sgl/SkBitmapProcState_sample.h',
        'sgl/SkBitmapSampler.cpp',
        'sgl/SkBitmapSampler.h',
        'sgl/SkBitmapSamplerTemplate.h',
        'sgl/SkBitmapShader.cpp',
        'sgl/SkBitmapShader.h',
        'sgl/SkBitmapShader16BilerpTemplate.h',
        'sgl/SkBitmapShaderTemplate.h',
        'sgl/SkBlitBWMaskTemplate.h',
        'sgl/SkBlitRow.h',
        'sgl/SkBlitRow_D16.cpp',
        'sgl/SkBlitRow_D4444.cpp',
        'sgl/SkBlitter.cpp',
        'sgl/SkBlitter.h',
        'sgl/SkBlitter_4444.cpp',
        'sgl/SkBlitter_A1.cpp',
        'sgl/SkBlitter_A8.cpp',
        'sgl/SkBlitter_ARGB32.cpp',
        'sgl/SkBlitter_RGB16.cpp',
        'sgl/SkBlitter_Sprite.cpp',
        'sgl/SkCanvas.cpp',
        'sgl/SkColor.cpp',
        'sgl/SkColorFilter.cpp',
        'sgl/SkColorTable.cpp',
        'sgl/SkCoreBlitters.h',
        'sgl/SkDeque.cpp',
        'sgl/SkDevice.cpp',
        'sgl/SkDither.cpp',
        'sgl/SkDraw.cpp',
        'sgl/SkDrawProcs.h',
        'sgl/SkEdge.cpp',
        'sgl/SkEdge.h',
        'sgl/SkFilterProc.cpp',
        'sgl/SkFilterProc.h',
        'sgl/SkFlattenable.cpp',
        'sgl/SkFP.h',
        'sgl/SkGeometry.cpp',
        'sgl/SkGeometry.h',
        'sgl/SkGlobals.cpp',
        'sgl/SkGlyphCache.cpp',
        'sgl/SkGlyphCache.h',
        'sgl/SkGraphics.cpp',
        'sgl/SkMask.cpp',
        'sgl/SkMaskFilter.cpp',
        'sgl/SkPackBits.cpp',
        'sgl/SkPaint.cpp',
        'sgl/SkPath.cpp',
        'sgl/SkPathEffect.cpp',
        'sgl/SkPathMeasure.cpp',
        'sgl/SkPixelRef.cpp',
        'sgl/SkProcSpriteBlitter.cpp',
        'sgl/SkPtrRecorder.cpp',
        'sgl/SkRasterizer.cpp',
        'sgl/SkRefCnt.cpp',
        'sgl/SkRegion_path.cpp',
        'sgl/SkScalerContext.cpp',
        'sgl/SkScan.cpp',
        'sgl/SkScan.h',
        'sgl/SkScan_Antihair.cpp',
        'sgl/SkScan_AntiPath.cpp',
        'sgl/SkScan_Hairline.cpp',
        'sgl/SkScan_Path.cpp',
        'sgl/SkScanPriv.h',
        'sgl/SkShader.cpp',
        'sgl/SkSpriteBlitter.h',
        'sgl/SkSpriteBlitter_ARGB32.cpp',
        'sgl/SkSpriteBlitter_RGB16.cpp',
        'sgl/SkSpriteBlitterTemplate.h',
        'sgl/SkString.cpp',
        'sgl/SkStroke.cpp',
        'sgl/SkStrokerPriv.cpp',
        'sgl/SkStrokerPriv.h',
        'sgl/SkTemplatesPriv.h',
        'sgl/SkTSearch.cpp',
        'sgl/SkTSort.h',
        'sgl/SkTypeface.cpp',
        'sgl/SkTypeface_fake.cpp',
        #'sgl/SkUnPreMultiply.cpp',
        'sgl/SkUtils.cpp',
        'sgl/SkWriter32.cpp',
        'sgl/SkXfermode.cpp',
        #'svg/SkSVG.cpp',
        #'svg/SkSVGCircle.cpp',
        #'svg/SkSVGCircle.h',
        #'svg/SkSVGClipPath.cpp',
        #'svg/SkSVGClipPath.h',
        #'svg/SkSVGDefs.cpp',
        #'svg/SkSVGDefs.h',
        #'svg/SkSVGElements.cpp',
        #'svg/SkSVGElements.h',
        #'svg/SkSVGEllipse.cpp',
        #'svg/SkSVGEllipse.h',
        #'svg/SkSVGFeColorMatrix.cpp',
        #'svg/SkSVGFeColorMatrix.h',
        #'svg/SkSVGFilter.cpp',
        #'svg/SkSVGFilter.h',
        #'svg/SkSVGG.cpp',
        #'svg/SkSVGG.h',
        #'svg/SkSVGGradient.cpp',
        #'svg/SkSVGGradient.h',
        #'svg/SkSVGGroup.cpp',
        #'svg/SkSVGGroup.h',
        #'svg/SkSVGImage.cpp',
        #'svg/SkSVGImage.h',
        #'svg/SkSVGLine.cpp',
        #'svg/SkSVGLine.h',
        #'svg/SkSVGLinearGradient.cpp',
        #'svg/SkSVGLinearGradient.h',
        #'svg/SkSVGMask.cpp',
        #'svg/SkSVGMask.h',
        #'svg/SkSVGMetadata.cpp',
        #'svg/SkSVGMetadata.h',
        #'svg/SkSVGPaintState.cpp',
        #'svg/SkSVGParser.cpp',
        #'svg/SkSVGPath.cpp',
        #'svg/SkSVGPath.h',
        #'svg/SkSVGPolygon.cpp',
        #'svg/SkSVGPolygon.h',
        #'svg/SkSVGPolyline.cpp',
        #'svg/SkSVGPolyline.h',
        #'svg/SkSVGRadialGradient.cpp',
        #'svg/SkSVGRadialGradient.h',
        #'svg/SkSVGRect.cpp',
        #'svg/SkSVGRect.h',
        #'svg/SkSVGStop.cpp',
        #'svg/SkSVGStop.h',
        #'svg/SkSVGSVG.cpp',
        #'svg/SkSVGSVG.h',
        #'svg/SkSVGSymbol.cpp',
        #'svg/SkSVGSymbol.h',
        #'svg/SkSVGText.cpp',
        #'svg/SkSVGText.h',
        #'svg/SkSVGUse.cpp',
        #'svg/SkSVGUse.h',
        #'text/ATextEntry.h',
        #'views/SkEvent.cpp',
        #'views/SkEventSink.cpp',
        #'views/SkMetaData.cpp',
        #'views/SkTagList.cpp',
        #'views/SkTagList.h',
        #'views/SkTextBox.cpp',
        #'xml/SkBML_Verbs.h',
        #'xml/SkBML_XMLParser.cpp',
        #'xml/SkDOM.cpp',
        #'xml/SkJS.cpp',
        #'xml/SkJSDisplayable.cpp',
        #'xml/SkParse.cpp',
        #'xml/SkParseColor.cpp',
        #'xml/SkXMLParser.cpp',
        #'xml/SkXMLPullParser.cpp',
        #'xml/SkXMLWriter.cpp',
      ],
      'include_dirs': [
        '..',
        'corecg',
        'include',
        'include/corecg',
        'picture',
        'sgl',
      ],
      'msvs_disabled_warnings': [4244, 4267,4345, 4390, 4554, 4800],
      'mac_framework_dirs': [
        '$(SDKROOT)/System/Library/Frameworks/ApplicationServices.framework/Frameworks',
      ],
      'defines': [
        'SK_BUILD_NO_IMAGE_ENCODE',
      ],
      'sources!': [
        'include/corecg/SkTypes.h',
        'precompiled.cc',
      ],
      'conditions': [
        [ 'OS != "mac"', {
          'sources/': [ ['exclude', '_mac\\.(cc|cpp)$'] ],
        }],
        [ 'OS != "linux"', {
          'sources/': [ ['exclude', '_linux\\.(cc|cpp)$'] ],
          'sources!': [
            'ext/GdkSkia.cc',
            'ports/SkFontHost_FreeType.cpp',
            'ports/SkFontHost_TryeType_Tables.cpp',
            'ports/SkFontHost_gamma_none.cpp',
            'ports/SkFontHost_fontconfig.cpp',
            'sgl/SkTypeface.cpp',
          ],
        }],
        [ 'OS != "win"', {
          'sources/': [ ['exclude', '_win\\.(cc|cpp)$'] ],
          'sources!': [
            'ext/vector_canvas.cc',
            'ext/vector_device.cc',
          ],
        }],
        [ 'OS == "mac"', {
          'defines': [
            'SK_BUILD_FOR_MAC',
          ],
        }],
        [ 'OS == "win"', {
          'sources!': [
            'images/SkMMapStream.cpp',
            'ports/SkFontHost_TrueType_Tables.cpp',
            'ports/SkThread_pthread.cpp',
            'ports/SkTime_Unix.cc',
          ],
          'configurations': {
            'Debug': {
              'msvs_precompiled_header': 'include/corecg/SkTypes.h',
              'msvs_precompiled_source': 'precompiled.cc',
            },
          },
        },],
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'include',
          'include/corecg',
        ],
      },
    },
  ],
}
