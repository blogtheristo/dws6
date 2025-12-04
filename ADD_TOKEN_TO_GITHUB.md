# Add Cloudflare Token to GitHub Secrets

**IMPORTANT:** Keep your token secure - never commit it to git!

---

## Step-by-Step Instructions

### 1. Go to GitHub Secrets Page
Open this URL in your browser:
**https://github.com/blogtheristo/dws6/settings/secrets/actions**

### 2. Add the Token
1. Click **"New repository secret"** button (top right)
2. **Name:** `CLOUDFLARE_API_TOKEN`
3. **Value:** (paste your token here - you have it from the previous message)
4. Click **"Add secret"**

### 3. Verify Zone IDs Exist
Check that these secrets already exist:
- `CLOUDFLARE_ZONE_ID_DWS10` = `3d1ee683d9436a21b2211002f5a16832`
- `CLOUDFLARE_ZONE_ID_ONELIFETIME` = `409f65ed2f9a97e329acbfe3887a629b`

If they're missing, add them as new secrets.

---

## Test After Adding

1. Make a small change to `dws10.com/index.html`
2. Commit and push:
   ```bash
   git add dws10.com/index.html
   git commit -m "Test cache purge"
   git push origin main
   ```
3. Check Actions: https://github.com/blogtheristo/dws6/actions
4. Look for "Purge Cloudflare Cache" workflow
5. Check logs - should see successful cache purge messages

---

## Security Note

✅ **Good:** Token is stored securely in GitHub Secrets  
✅ **Good:** Token is never exposed in logs or code  
❌ **Bad:** Never commit tokens to git files  
❌ **Bad:** Never share tokens in public places

Your token is safe once added to GitHub Secrets!

